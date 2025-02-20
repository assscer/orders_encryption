import redis
import json

cache = redis.Redis(host="localhost", port=6379, db=0)

def set_cache(key, value, timeout=60):
    cache.set(key, json.dumps(value), ex=timeout)

def get_cache(key):
    data = cache.get(key)
    return json.loads(data) if data else None
