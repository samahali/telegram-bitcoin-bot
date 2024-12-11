# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock ./

# Install pipenv
RUN pip install pipenv

# Install the dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["pipenv", "run", "python", "main.py"]