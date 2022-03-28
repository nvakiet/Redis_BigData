# import modules
from pyspark.sql import SparkSession
from redis import Redis

# set the app name and Redis address
APPNAME = "ClickQuery"
RHOST = "127.0.0.1"
RPORT = "6379"

def main():
    try:
        # init spark session
        spark = SparkSession.builder\
            .appName(APPNAME)\
            .master("local[*]")\
            .getOrCreate()

        # Connect to Redis
        r = Redis(RHOST, RPORT)

        # Run a redis streaming query
        r.xadd("clicks", {"asset": "testAsset", "cost": 100}, maxlen=1000000)

        # Create a table view of Redis data, only need to call once when program starts
        df = spark.read.format("org.apache.spark.sql.redis").schema("asset STRING, count INT").option("table", "click").load()
        
        # should use an event scheduler library to run the content of the loop every second instead of this
        for i in range(1000): 
            df.select("*").show() # Call the select query again whenever needed, it will sync with Redis data
            
        # end program
        r.close()
        spark.stop()
        return 0
    except Exception as e:
        print(e)

# Starting point for PySpark
if __name__ == '__main__':
    main()