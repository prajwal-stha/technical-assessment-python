# Dockerfile

# Pull base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /src

# Install dependencies
COPY requirements.txt /src
RUN pip install -r requirements.txt

# Copy project
COPY . /src/

ENTRYPOINT sh -c "python manage.py runserver 0.0.0.0:8000"
