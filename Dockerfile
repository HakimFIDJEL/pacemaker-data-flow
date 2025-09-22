# Dockerfile

FROM python:3.11-slim

RUN apt-get update -y && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY producer.py /app/

CMD ["python", "-u", "producer.py"]
