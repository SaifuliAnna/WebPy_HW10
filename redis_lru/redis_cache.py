import redis
from redis_lru import RedisLRU
import timeit

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def f(x, y):
    z = ((x ** y) / 3 * (4 - (2 + y)))
    return f'Результат: {z}'


start_time = timeit.default_timer()
print(f(3, 8))
print(f'Duration: {timeit.default_timer() - start_time}')

start_time = timeit.default_timer()
print(f(3, 8))
print(f'Duration: {timeit.default_timer() - start_time}')

