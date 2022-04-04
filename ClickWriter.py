
"""
# Title : Web Click Processing Using Redis And Spark
# Author : Ngo Van Anh Kiet
# Date: 23/03/2022
"""

from redis import Redis

# A custom ForeachWriter class to be used in spark-redis query
class ClickWriter:
    # Class constructor
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.redisClient = None
    
    # Connect to a redis instance at the initialized host address and port
    def connect(self):
        self.redisClient = Redis(self.host, self.port)
    
    def open(self, partition_id, epoch_id):
        return True
        
    # Method to write each row to Redis
    def process(self, row):
        # Retrieve row attributes
        asset = str(row["asset"])
        print(row)
        
        # Write the values to Redis
        if self.redisClient is None:
            self.connect()
        self.redisClient.hmset("click:"+asset, row.asDict())
        self.redisClient.expire("click:"+asset, 300)

    def close(self, error):
        pass
