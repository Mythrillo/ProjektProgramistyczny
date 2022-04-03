FROM python:3.10.2

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ARG PORT

ENV PORT=${PORT:-8080}

CMD alembic upgrade head ; uvicorn main:app --host 0.0.0.0 --port $PORT
