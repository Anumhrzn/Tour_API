"""SETTINGS
Settings loaders using Pydantic BaseSettings classes (load from environment variables / dotenv file)
"""

# # Installed # #
import pydantic


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class APISettings(BaseSettings):
    title: str = "TOUR API"
    host: str = "localhost"
    port: int = 5000

    class Config(BaseSettings.Config):
        env_prefix = "API_"


# class DBSettings(BaseSettings):
#     provider:str
#     user:str
#     password:str
#     host:str
#     port:int
#     database:str

#     class Config(BaseSettings.Config):
#         env_prefix = "DB_"


api_settings = APISettings()
# db_settings = DBSettings()
