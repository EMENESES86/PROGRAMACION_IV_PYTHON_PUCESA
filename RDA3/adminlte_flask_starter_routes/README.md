# Proyecto Base Flask + Blueprints + AdminLTE

Este proyecto es una plantilla básica de Flask organizada profesionalmente, lista para ser usada en clases de **Programación IV**.

---

## 📌 Objetivos de esta estructura

- Separar el código de las rutas usando **Blueprints**.
- Mantener el código organizado, modular y escalable.
- Integrar AdminLTE 3 para una interfaz profesional.
- Facilitar el uso de `url_for` correctamente con Blueprints.

---

## 📂 Estructura del proyecto

```bash
adminlte_flask_starter_routes/
│
├── app.py               # Archivo principal de la aplicación
├── routes/              # Carpeta de rutas (Blueprints)
│   ├── __init__.py      # Importa y registra todos los Blueprints
│   ├── home_routes.py   # Rutas relacionadas al Home
│   └── user_routes.py   # Rutas relacionadas a Usuarios
│
├── templates/           # Templates HTML (con AdminLTE)
│   ├── base.html        # Plantilla base heredada por otras páginas
│   ├── home.html        # Página de inicio
│   └── usuarios.html    # Página de usuarios
│
├── static/              # Archivos estáticos (CSS, JS, imágenes)
│   └── adminlte/        # Archivos de AdminLTE
│
└── README.md            # Este archivo de documentación
```

# ¿Qué es un Blueprint?

    En Flask, los Blueprints permiten organizar la aplicación en módulos independientes.

    Cada módulo tiene sus propias rutas, controladores, plantillas, etc.

    Ayudan a mantener el código limpio a medida que crece la aplicación.

# ¿Para qué sirve __init__.py dentro de routes/?

    Este archivo inicializa el paquete routes.

    Se encarga de importar cada blueprint y registrarlo en la aplicación principal.

    Permite que Flask conozca todas las rutas sin tenerlas todas mezcladas en app.py.