FROM python:3

RUN mkdir /code
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /code/
ADD src/.env /code/src/

RUN pip install --upgrade pip flake8
RUN pip install -r requirements.txt

ADD . /code/

COPY docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT [ "docker-entrypoint.sh" ]

RUN flake8 --ignore=F403,F401,F405,F841,E501,W503