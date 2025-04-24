class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0

    def estado(self):
        return "Aprobado" if self.promedio() >= 7 else "Reprobado"

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.promedio():.2f}")
        print(f"Estado: {self.estado()}\n")
