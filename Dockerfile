FROM python:3.10-slim

WORKDIR /app

# Copiar e instalar dependencias
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación, pipelines y datos
COPY backend/ ./backend/
COPY pipelines/ ./pipelines/
COPY database/ ./database/
COPY data/ ./data/

# Variables de entorno y puerto
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
