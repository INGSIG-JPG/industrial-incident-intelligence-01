FROM python:3.10-slim

WORKDIR /app

# Copiar e instalar dependencias
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación, pipelines, base de datos y datos crudos
COPY backend/ ./backend/
COPY pipelines/ ./pipelines/
COPY database/ ./database/
COPY data/ ./data/

# Variables de entorno y puerto
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

# Comando de inicio: ejecuta la ingesta de datos y luego levanta la API
CMD python pipelines/ingest_data.py && uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
