# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev zlib-dev jpeg-dev gcc musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D django
RUN chown -R django:django /vol/
RUN chmod -R 755 /vol/web
USER django