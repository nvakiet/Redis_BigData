"""
# Title : Web Click Processing Using Redis And Spark
# Author : Ngo Van Anh Kiet
# Date: 23/03/2022
# Usage : spark-submit click_count.py > ./click_count.log 2>&1 &
"""

# import modules
from pyspark.sql import SparkSession
import sys,logging
from datetime import datetime

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
APPNAME = "ClickProcessing"

def main():
    # start spark code
    spark = SparkSession.builder.appName(APPNAME + "_" + str(dt_string)).getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    logger.info("Starting spark application")

    # do some tasks here


    
    # end spark code
    logger.info("Ending spark application")
    spark.stop()
    return 0

# Starting point for PySpark
if __name__ == '__main__':
    main()
    