# Importa la función para renderizar plantillas HTML
from flask import render_template

# Importa el modelo Usuario definido con SQLAlchemy
from models.models import Usuario

# Importa la clase datetime para obtener la fecha y hora actual
from datetime import datetime

# Importa las funciones auxiliares desde utils.helpers
from utils.helpers import saludar, formatear_fecha

# Función que consulta todos los usuarios desde la base de datos
# y pasa la lista junto con la fecha actual formateada a la plantilla
def obtener_usuarios():
    usuarios = Usuario.query.all()  # Consulta todos los registros de la tabla 'usuario'
    fecha = formatear_fecha(datetime.now())  # Obtiene la fecha actual y la formatea
    # Renderiza la plantilla 'usuarios.html' con la lista de usuarios y la fecha
    return render_template("usuarios.html", usuarios=usuarios, fecha=fecha)

# Función que genera un mensaje de saludo personalizado con el nombre dado
# y lo pasa a la plantilla 'saludo.html'
def saludar_usuario(nombre):
    mensaje = saludar(nombre)  # Usa el helper para generar el mensaje: "Hola, <nombre>!"
    return render_template("saludo.html", mensaje=mensaje)  # Muestra el mensaje en la vista
