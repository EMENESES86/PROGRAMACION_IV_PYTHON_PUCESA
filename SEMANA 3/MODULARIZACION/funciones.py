from estudiante import Estudiante

# Lista global para guardar estudiantes
estudiantes = []

def registrar_estudiante():
    nombre = input("Nombre del estudiante: ")
    matricula = input("Matrícula: ")
    carrera = input("Carrera: ")
    estudiante = Estudiante(nombre, matricula, carrera)
    estudiantes.append(estudiante)
    print("Estudiante registrado con éxito.\n")

def buscar_estudiante(matricula):
    for est in estudiantes:
        if est.matricula == matricula:
            return est
    return None

def agregar_nota_estudiante():
    matricula = input("Ingrese la matrícula del estudiante: ")
    estudiante = buscar_estudiante(matricula)
    if estudiante:
        try:
            nota = float(input("Ingrese la nota: "))
            estudiante.agregar_nota(nota)
            print("Nota agregada con éxito.\n")
        except ValueError:
            print("Nota inválida. Debe ser un número.\n")
    else:
        print("Estudiante no encontrado.\n")

def mostrar_estudiante():
    matricula = input("Ingrese la matrícula del estudiante: ")
    estudiante = buscar_estudiante(matricula)
    if estudiante:
        estudiante.mostrar_datos()
    else:
        print("Estudiante no encontrado.\n")

def mostrar_todos():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
    for est in estudiantes:
        est.mostrar_datos()
