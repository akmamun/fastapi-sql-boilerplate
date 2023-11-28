from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app_name.routes import routers

app = FastAPI(routes=routers)

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
    app.run(app, host="0.0.0.0", port=8000, debug=True)