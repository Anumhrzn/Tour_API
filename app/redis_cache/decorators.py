import json

from app.redis_cache import get_cache
from fastapi_cache.backends.redis import RedisCacheBackend
from app.settings import configs

redis_settings = configs.redis_settings


def cache(expire: int = -1):
    """
    Decorator for caching api response. It re-fetches again after the expiry time

   Args:
      expire (int): Expire time in seconds, Defaults expire to infinity
    """

    def decorator(func):
        async def wrapper(*args, **kwargs):
            redis_cache: RedisCacheBackend = get_cache()
            cache_key = f"{func.__name__}{json.dumps(args)}{json.dumps(kwargs)}"
            cached_data = await redis_cache.get(cache_key)
            if cached_data:
                return json.loads(cached_data)
            returned_value = func(*args, **kwargs)
            await redis_cache.set(cache_key, json.dumps(returned_value))
            if (expire > 0):
                await redis_cache.expire(cache_key, expire)
            return returned_value

        return wrapper

    return decorator


@cache(expire=10)
async def default(name: str, last_name: str):
    return name


if __name__ == '__main__':
    default('nabin', last_name='kawan')
