# Importa la instancia de SQLAlchemy desde el archivo extensions.py
from extensions import db

# Define el modelo 'Usuario', que representará la tabla 'usuario' en la base de datos
class Usuario(db.Model):
    # Columna 'id' será la clave primaria y se autoincrementa automáticamente
    id = db.Column(db.Integer, primary_key=True)
    
    # Columna 'nombre' almacenará texto de hasta 100 caracteres, y no puede ser nula
    nombre = db.Column(db.String(100), nullable=False)
    
    # Columna 'email' almacenará texto de hasta 120 caracteres, debe ser único y no nulo
    email = db.Column(db.String(120), unique=True, nullable=False)
