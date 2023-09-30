#Select the base image
FROM python:3.10 as python-base

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get -y dist-upgrade
RUN apt-get install -y build-essential

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code
COPY . /code/
RUN ls
RUN pip install -r requirements.txt
ENTRYPOINT [ "/code/docker/entrypoint.sh" ]
