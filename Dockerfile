FROM python:3.10.7-slim-buster

ENV PYTHONUNBUFFERED 1
# RUN apt-get install libmysqlclient-dev


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser user
USER user