# Importa la clase SQLAlchemy, que permite usar un ORM (Object Relational Mapper)
# para interactuar con la base de datos en Flask de forma orientada a objetos
from flask_sqlalchemy import SQLAlchemy

# Crea una instancia global de SQLAlchemy llamada 'db'
# Esta instancia será compartida por todos los modelos y controladores que necesiten acceso a la base de datos
db = SQLAlchemy()
