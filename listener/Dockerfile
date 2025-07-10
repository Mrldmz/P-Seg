FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código del servidor
COPY server.py .
COPY decrypt.py .

# Crear directorios para datos
RUN mkdir -p /app/data/encrypted /app/data/decrypted /app/logs

# Exponer puerto
EXPOSE 5000

# Comando por defecto
CMD ["python", "server.py"]
