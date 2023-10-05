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
RUN python -m pip install --index-url https://test.pypi.org/simple/ --no-deps --no-build-isolation haze-uttam-users
# Copy project
COPY . /src/

RUN python manage.py makemigrations
RUN python manage.py migrate
ENTRYPOINT sh -c "python manage.py runserver 0.0.0.0:8000"
