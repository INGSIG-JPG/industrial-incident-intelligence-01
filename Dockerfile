FROM python:3.10-slim

WORKDIR /app

# Copiar requerimientos e instalar dependencias
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del backend, la base de datos y los pipelines
COPY backend/ ./backend/
COPY database/ ./database/
COPY pipelines/ ./pipelines/

# Ejecutar la ingesta para poblar la base de datos durante la construcción
RUN python pipelines/ingest_data.py

EXPOSE 8000

# Ejecutar el servidor Uvicorn apuntando al backend
WORKDIR /app/backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
