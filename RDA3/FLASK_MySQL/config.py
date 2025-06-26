# Importa el módulo os para acceder a las variables de entorno del sistema
import os

# Importa la función load_dotenv para cargar las variables desde el archivo .env
from dotenv import load_dotenv

# Carga automáticamente las variables definidas en el archivo .env al entorno del sistema
load_dotenv()

# Define una clase de configuración para la aplicación Flask
class Config:
    # Construye la URI de conexión a MySQL usando las variables de entorno cargadas
    # Formato: mysql+pymysql://usuario:contraseña@host:puerto/nombre_base
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    
    # Desactiva el rastreo de modificaciones de objetos (recomendado para rendimiento)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
