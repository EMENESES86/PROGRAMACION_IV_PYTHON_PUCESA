# Definimos una clase llamada Persona
class Persona:
    # Este es el constructor de la clase, se llama automáticamente al crear un objeto
    def __init__(self, nombre, edad):
        # Asignamos el valor recibido 'nombre' al atributo 'self.nombre' del objeto
        self.nombre = nombre
        # Asignamos el valor recibido 'edad' al atributo 'self.edad' del objeto
        self.edad = edad

    # Definimos un método que pertenece a la clase Persona
    def saludar(self):
        # Devuelve un texto con los datos de la persona
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."


# -------------------------------
# Aquí comienza el archivo operaciones.py
# -------------------------------

# Definimos una función externa que recibe una edad y devuelve True si es mayor o igual a 18
def es_mayor_de_edad(edad):
    return edad >= 18  # Devuelve True si la persona es mayor de edad, False si no


# -------------------------------
# Código para probar las clases y funciones
# -------------------------------

# Creamos un objeto 'p' de la clase Persona, con nombre "Edison" y edad 37
p = Persona("Edison", 37)

# Llamamos al método saludar del objeto 'p' y lo mostramos en pantalla
print(p.saludar())  # Salida esperada: "Hola, me llamo Edison y tengo 37 años."

# Llamamos a la función externa 'es_mayor_de_edad' pasando como argumento la edad del objeto 'p'
print("¿Es mayor de edad?", es_mayor_de_edad(p.edad))  # Salida esperada: True
