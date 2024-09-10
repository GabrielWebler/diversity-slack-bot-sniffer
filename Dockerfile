FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install slack_sdk

EXPOSE 5000

CMD ["python", "app.py"]