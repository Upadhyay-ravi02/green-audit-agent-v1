FROM python:3.10-slim

WORKDIR /app

# Required libraries install
RUN apt-get update && apt-get install -y \
    libpng-dev libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

LABEL openenv="true"
ENV PYTHONUNBUFFERED=1

# Exposing port for HF Space health check
EXPOSE 7860

CMD ["python", "inference.py"]
