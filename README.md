# FastAPI Micro Service with Docker and Asynchronous SQLAlchemy

This repository provides a template for building a FastAPI microservice using Docker with asynchronous SQLAlchemy for efficient database operations.

###  Installation Instructions

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

### Run Locally
- To run the service locally, use the following command:
    ```sh
    uvicorn server:app --reload
    ```
### Run with Docker
- To run the service using Docker, use the following command:
     ```sh
       sudo docker-compose up -d --build
     ```
### Run Docker Compose for Production Build
- Ensure that you have [Docker](https://docs.docker.com/engine/install) and [Docker Compose](https://docs.docker.com/compose/install/) installed

## Project Structure
```
├── app_name
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── item_controller.py
│   ├── models
│   │   ├── item_models.py
│   ├── repositories
│   │   ├── __init__.py
│   │   ├── item_repository.py
│   ├── routes.py
│   └── tests
├── app.py
├── config
│   ├── config.py
│   └── db.py
├── db
│   ├── alchemy_repository.py
├── docker-compose.yml
├── Dockerfile
├── helpers
│   ├── env.py
│   └── pagination.py
├── locust.py
├── README.md
├── requirements.txt
└── scripts
    └── migrate.py
```
