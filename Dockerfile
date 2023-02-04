FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential \
        python-dev \
        default-libmysqlclient-dev


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN chmod 666 /app/app/settings/celerybeat-schedule

RUN adduser user
USER user

EXPOSE 8000