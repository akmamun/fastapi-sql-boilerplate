# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set environment variables to ensure Python runs in unbuffered mode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy only the requirements file initially to leverage Docker caching
COPY requirements.txt /app/requirements.txt

# Install requirements
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that your FastAPI application will run on
EXPOSE 8000
