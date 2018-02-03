# Dockerfile inspired by "Timothy Ko <tk2@illinois.edu>" from https://medium.freecodecamp.org/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a

FROM python:3.6

RUN apt-get update

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install pip-tools
RUN pip-compile > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV="docker"

EXPOSE 5000
