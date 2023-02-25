"""APP
FastAPI app definition, initialization and definition of routes
"""

# # Installed # #
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket
from app.routers import users, recommendation, places, distance, weather
from app.db import init_local_db

from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# # Package # #

load_dotenv()
init_local_db()

app = FastAPI(
    title="Tour api"
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

# app.include_router(candidates.router)
# app.include_router(voters.router)
# app.include_router(admin.router)
# app.include_router(file.router)
# app.include_router(login.router)


# def run():
#     """Run the API using Uvicorn"""
#     uvicorn.run(
#         'app:app',
#         port=api_settings.port,
#         host=api_settings.host,
#         reload=True,
#     )

if __name__ == "__main__":
    print("running")
    # run()
    # uvicorn.run('app:app', host='localhost', port=8000,reload=True)
