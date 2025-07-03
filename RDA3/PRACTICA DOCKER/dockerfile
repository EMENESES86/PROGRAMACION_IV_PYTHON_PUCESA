# Usa una imagen oficial de Python como base
FROM python:3.12-alpine

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto correcto
EXPOSE 4000

# Comando por defecto para correr la aplicación
CMD ["python", "app.py"]
