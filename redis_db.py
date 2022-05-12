import redis
import json


class RedisDB:
    def __init__(self, host="redis-16819.c85.us-east-1-2.ec2.cloud.redislabs.com", port=16819, db=0, password="iuaEzgb9qfWREWqVoiBYnR1DMpLLoJez") -> None:
        self.redisDB = redis.Redis(
            host=host, port=port, db=db, password=password)

    def saveCart(self, userId: str, value: any):
        self.redisDB.set(userId, json.dumps(value))

    def getCart(self, userId: str):
        return json.loads(self.redisDB.get(userId))
