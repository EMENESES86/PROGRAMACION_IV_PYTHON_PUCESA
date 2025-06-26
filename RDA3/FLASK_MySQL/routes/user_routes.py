from flask import Blueprint
from controllers.user_controller import obtener_usuarios, saludar_usuario

user_bp = Blueprint("usuarios", __name__)

@user_bp.route('/')
def index():
    return "Bienvenido a la aplicación Flask de ejemplo"

@user_bp.route('/usuarios/')
def listar_usuarios():
    return obtener_usuarios()

@user_bp.route('/saludo/<nombre>')
def mostrar_saludo(nombre):
    return saludar_usuario(nombre)