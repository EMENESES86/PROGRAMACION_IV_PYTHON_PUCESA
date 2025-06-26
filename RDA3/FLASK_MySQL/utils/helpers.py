# Función que genera un saludo personalizado con el nombre proporcionado
# Parámetros:
#   nombre (str): el nombre de la persona a saludar
# Retorna:
#   str: mensaje en formato "Hola, <nombre>!"
def saludar(nombre):
    return f"Hola, {nombre}!"


# Función que recibe un objeto de tipo datetime y lo convierte a una cadena con formato dd/mm/aaaa
# Parámetros:
#   fecha (datetime): fecha que se desea formatear
# Retorna:
#   str: fecha como cadena en formato día/mes/año (por ejemplo, "25/06/2025")
def formatear_fecha(fecha):
    return fecha.strftime('%d/%m/%Y')

