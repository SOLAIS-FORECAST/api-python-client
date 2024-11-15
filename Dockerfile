# For CI/CD Testing
FROM python:3.10-slim

WORKDIR /home/app

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .