"""
# Title : Web Click Processing Using Redis And Spark
# Author : Ngo Van Anh Kiet
# Date: 23/03/2022
# Usage :
    * To run spark task in the background and write to log files
    spark-submit --jars lib/spark-redis.jar ClickAnalyzer.py > ./click_count.log 2>&1 &
    * To run spark task in the foreground and logs to the console
    spark-submit --jars lib/spark-redis.jar ClickAnalyzer.py
"""

# import modules
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import sys,logging
from datetime import datetime
from ClickWriter import ClickWriter

# Logging configuration
formatter = logging.Formatter('[%(asctime)s] %(levelname)s @ line %(lineno)d: %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# current time variable to be used for logging purpose
dt_string = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
# set the app name
APPNAME = "ClickAnalyzer"
# redis instance address
RHOST = "127.0.0.1"
RPORT = "6379"

def main():
    # init spark session
    spark = SparkSession.builder\
        .appName(APPNAME + "_" + str(dt_string))\
        .master("local[*]")\
        .config("spark.redis.host", RHOST)\
        .config("spark.redis.port", RPORT)\
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    logger.info("Starting spark application")

    # setup stream schema
    clicks = spark.readStream.format("redis").option("stream.keys", "clicks")\
        .schema(StructType([
            StructField("asset", StringType()),
            StructField("cost", LongType())
        ]))\
        .load()

    # create DataFrame contains data grouped by asset counts
    byasset = clicks.groupBy("asset").count()
    
    # create a writer to save each data row to Redis
    clickWriter = ClickWriter(RHOST, int(RPORT))
    
    # start a Spark Structured Streaming query to update count result to Redis
    # using a custom ForEach writer or just print the result to console
    query = byasset\
            .writeStream\
            .outputMode("update")\
            .foreach(clickWriter)\
            .start()
    
    query.awaitTermination()
    
    # end spark code
    logger.info("Ending spark application")
    spark.stop()
    return 0

# Starting point for PySpark
if __name__ == '__main__':
    main()
    