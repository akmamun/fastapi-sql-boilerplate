import logging
from config.config import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from example_app_name.routes import routers

app = FastAPI(routes=routers)

# Add more apps by importing their routers and appending to the apps list
# from another_app_name.routes import routers as another_app_routers
# all_routes = [example_routers, another_app_routers]

# app = FastAPI(routes=all_routes)

# CORS settings
origins = [
    "*"
    # Add other allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    host = config['http']['host']
    port = config['http']['port']

    app.run(app, host=host, port=port)
    logging.info("Server started. Listening on %s:%s", host, port)
