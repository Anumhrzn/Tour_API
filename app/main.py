"""APP
FastAPI app definition, initialization and definition of routes
"""

# # Installed # #
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket
from app.routers import users, recommendation, places, distance, weather, rating
from app.db import init_local_db

from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import caches, close_caches
from fastapi_cache.backends.redis import CACHE_KEY, RedisCacheBackend
from app.settings import configs

api_settings = configs.api_settings
redis_settings = configs.redis_settings

# # Package # #

load_dotenv()
init_local_db()

app = FastAPI(
    title=api_settings.title,
    description=api_settings.description,
    version=api_settings.version,
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# creating different application for '/static'
app.mount('/static', StaticFiles(directory='static'))


@app.get("/", name="root", tags=["Root"])
async def root():
    return {"message": f"Welcome to Tour API {app.version}"}


app.include_router(users.router)
app.include_router(recommendation.router)
app.include_router(places.router)
app.include_router(distance.router)
app.include_router(weather.router)
app.include_router(rating.router)


@app.on_event('startup')
async def on_startup() -> None:
    rc = RedisCacheBackend(redis_settings.url)
    caches.set(CACHE_KEY, rc)


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await close_caches()


if __name__ == "__main__":
    print("running")
    # run()
    # uvicorn.run('app:app', host='localhost', port=8000,reload=True)
