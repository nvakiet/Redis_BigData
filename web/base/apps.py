from django.apps import AppConfig
from redis import Redis

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    
    # def ready(self):
    #     self.redisClient = Redis(self.host, self.port)
    #     self.redisClient.xadd("clicks", [{"asset": "Ad1"}, {
    #                           "cost": 29}], max_length=1000000)
# Code connecting Redis & Spark
