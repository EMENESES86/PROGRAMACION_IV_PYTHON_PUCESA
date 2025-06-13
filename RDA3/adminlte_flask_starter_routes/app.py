from flask import Flask

# Importamos las rutas desde la carpeta routes
from routes import register_blueprints

app = Flask(__name__)

# Registramos los blueprints
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
