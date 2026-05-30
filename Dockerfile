# pull official base image
FROM python:3.13-slim

#  env variables
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONBUFFERED = 1

# work directory
WORKDIR /app

# install netcat for the entrypoint health check
RUN apt-get update && apt-get install -y netcat-openbsd

# install dependencies
COPY backend/requirements/base.txt .
RUN pip install --upgrade pip && pip install -r base.txt

# copy project
COPY backend/ .

# run gunicorn
CMD [ "gunicon", "config.wsgi:application", "--bind", "0.0.0:8000" ]
