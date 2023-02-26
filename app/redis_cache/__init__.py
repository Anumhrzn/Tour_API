from fastapi_cache import caches
from fastapi_cache.backends.redis import CACHE_KEY


def get_cache():
    return caches.get(CACHE_KEY)
