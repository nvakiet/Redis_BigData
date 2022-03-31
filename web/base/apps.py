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
        print(self.spark.sparkContext.getConf().getAll())