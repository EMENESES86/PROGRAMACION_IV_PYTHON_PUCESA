from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)
# create_user_bp = Blueprint('create_usuarios', __name__, url_prefix='//users/create_usuarios')

@user_bp.route('/users')
def users():
    return render_template("usuarios.html")


@user_bp.route('/users/crear_usuarios')
def crear_usuarios():
    return render_template("create_users.html")

# @create_user_bp.route('/')
# def create_users():
#     return render_template("create_users.html")