"""SETTINGS
Settings loaders using Pydantic BaseSettings classes (load from environment variables / dotenv file)
"""

# # Installed # #
import pydantic


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class ApiSettings(BaseSettings):
    title: str = "TOUR API"
    host: str = "localhost"
    port: int = 5000

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class RedisSettings(BaseSettings):
    url: str = "redis://127.0.0.1:6379"
    cache_ttl: int = 5

    class Config:
        env_prefix = "REDIS_"


# class DBSettings(BaseSettings):
#     provider:str
#     user:str
#     password:str
#     host:str
#     port:int
#     database:str

#     class Config(BaseSettings.Config):
#         env_prefix = "DB_"

class Settings(BaseSettings):
    api_settings: ApiSettings = ApiSettings()
    redis_settings: RedisSettings = RedisSettings()


# db_settings = DBSettings()

def get_configs():
    return Settings()


configs = get_configs()
