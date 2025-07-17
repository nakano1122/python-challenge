FROM python:3.10-slim

WORKDIR /app
RUN apt update && apt install -y git tree wget
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
