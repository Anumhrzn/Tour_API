import uvicorn

# # Package # #
from app.settings import api_settings


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        'app.main:app',
        port=api_settings.port,
        host='192.168.1.103',
        reload=True,
    )


if __name__ == '__main__':
    run()
