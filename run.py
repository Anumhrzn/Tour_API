import uvicorn

# # Package # #
from app.settings import configs

api_settings = configs.api_settings


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        'app.main:app',
        port=api_settings.port,
        # host='192.168.40.245',
        reload=True,
    )


if __name__ == '__main__':
    run()
