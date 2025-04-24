# def suma():
#     return 2 + 2

# print(suma())  

# def resta():
#     print(5 - 3) 

# resta()


# Definimos una CLASE llamada 'Persona'
class Persona:
    # Este es el CONSTRUCTOR de la clase. Se ejecuta automáticamente al crear un objeto.
    # 'nombre' y 'edad' son PARÁMETROS que se reciben al crear la persona.
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo del objeto que guarda el nombre
        self.edad = edad      # Atributo del objeto que guarda la edad

    # Este es un MÉTODO de la clase. Los métodos son funciones que pertenecen a la clase.
    # Siempre reciben 'self' como primer parámetro, que representa al propio objeto.
    def saludar(self):
        # Este método devuelve un texto usando los atributos del objeto
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."




# Definimos la clase Estudiante que HEREDA de la clase Persona
class Estudiante(Persona):
    
    # Constructor de la clase Estudiante
    def __init__(self, nombre, edad, carrera):
        # Llamamos al constructor de la clase base (Persona) usando super()
        super().__init__(nombre, edad)
        # Agregamos un nuevo atributo propio de la clase Estudiante
        self.carrera = carrera

    # Método propio de la clase Estudiante
    def datos_completos(self):
        # Usa el método saludar heredado de Persona y añade el atributo carrera
        return f"{self.saludar()} Estudio {self.carrera}."

# Creamos un objeto 'est1' de la clase Estudiante
est1 = Estudiante("Ana", 21, "Ingeniería de Software")
est2 = Estudiante("Luis", 22, "Matemáticas")

# Llamamos al método 'datos_completos' y mostramos el resultado
print(est1.datos_completos())
print(est2.datos_completos())