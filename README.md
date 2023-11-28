# FastAPI MicroService with Docker and Asynchronous SQLAlchemy

This repository provides a template for building a FastAPI microservice using Docker with asynchronous SQLAlchemy for efficient database operations.

###  Installation Instructions
**Using Docker:**
- To run the service using Docker, use the following command:
     ```sh
     sudo docker-compose up --build
     ```

**Run Locally:**

- Create a [virtual environment](https://docs.python.org/3/library/venv.html)
- Install the Python dependencies with
     ```sh
     pip install -r requirements.txt
    ```
- Copy the .env.example file as .env
    ```sh
    cp .env.example .env
    ```
- Ensure that you fill in all the valid environment properties in the .env file.

## Setup and Configuration:

Please note that when forking and intending to use it, follow instruction

- Delete the `example_app_name` folder
- Remove the line `from example_app_name.routes import routers` in `main.py`

Your setup is now ready for smooth use.

### Run Locally
- To run the service locally, use the following command:
    ```sh
    uvicorn main:app --reload
    ```

### Run Docker Compose for Production Build
- Ensure that you have [Docker](https://docs.docker.com/engine/install) and [Docker Compose](https://docs.docker.com/compose/install/) installed

## Project Structure

```
├── app_name
│   ├── controllers
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── repositories
│   │   └── __init__.py
│   ├── routes.py
│   └── tests
│       └── __init__.py
├── config
│   ├── config.py
│   └── db.py
├── db
│   └── alchemy_repository.py
├── docker-compose.yml
├── Dockerfile
├── example_app_name
│   ├── controllers
│   │   ├── __init__.py
│   │   └── item_controller.py
│   ├── models
│   │   └── item_models.py
│   ├── repositories
│   │   ├── __init__.py
│   │   └── item_repository.py
│   ├── routes.py
│   └── tests
│       └── __init__.py
├── helpers
│   ├── env.py
│   └── pagination.py
├── locust.py
├── main.py
├── README.md
├── requirements.txt
└── scripts
    └── migrate.py
```
