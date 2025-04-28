# Usa una imagen oficial de Python liviana
FROM python:3.11-slim

# Instala ffmpeg (necesario para yt-dlp)
RUN apt-get update && apt-get install -y ffmpeg

# Crea un directorio de trabajo
WORKDIR /app

# Copia el proyecto al contenedor
COPY . .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que tu app usará
EXPOSE 10000

# Corre el servidor
CMD ["python", "app.py"]
