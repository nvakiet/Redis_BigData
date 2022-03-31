from django.apps import AppConfig
from pyspark.sql import SparkSession
from redis import Redis

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    
    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        self.spark = None
        self.rd = None
    
    def ready(self):
        self.spark = SparkSession.builder.master("local[*]")\
            .config("spark.jars", "lib/spark-redis.jar")\
            .getOrCreate()
        self.rd = Redis("127.0.0.1", "6379")
        
        self.spark.sparkContext.setLogLevel("WARN")
        self.spark.sql("CREATE TABLE IF NOT EXISTS clicks(asset STRING, count INT) USING org.apache.spark.sql.redis OPTIONS (table 'click')")