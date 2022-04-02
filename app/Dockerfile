FROM python:3.10.2

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ARG PORT
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_URL
ARG POSTGRES_DB_NAME_NAME
ARG POSTGRES_PORT

ENV PORT=${PORT:-80}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_URL=${POSTGRES_URL}
ENV POSTGRES_DB_NAME=${POSTGRES_DB_NAME}
ENV POSTGRES_PORT=${POSTGRES_PORT}

CMD chmod a+x wait-for-it.sh ; ./wait-for-it.sh $POSTGRES_URL:$POSTGRES_PORT ; alembic upgrade head ; uvicorn main:app --host 0.0.0.0 --port $PORT
