# syntax=docker/dockerfile:1
FROM --platform=$TARGETPLATFORM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY Procfile .
EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:${PORT:-8080}", "app:app"]
