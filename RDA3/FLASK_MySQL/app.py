# Importa la clase Flask para crear la aplicación web
from flask import Flask

# Importa la configuración desde el archivo config.py (lee las variables de entorno)
from config import Config

# Importa la instancia de SQLAlchemy desde extensions.py
from extensions import db

# Función de fábrica para crear y configurar la aplicación Flask
def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Carga la configuración desde la clase Config (incluye conexión a base de datos)
    app.config.from_object(Config)

    # Inicializa la extensión de SQLAlchemy con la app
    db.init_app(app)

    # Importa y registra el blueprint de rutas de usuarios
    from routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    # Devuelve la aplicación completamente configurada
    return app

# Crea la aplicación usando la función de fábrica
app = create_app()

# Ejecuta la aplicación si se llama directamente este archivo
if __name__ == '__main__':
    # Inicia el servidor en modo debug (útil para desarrollo)
    app.run(debug=True)
