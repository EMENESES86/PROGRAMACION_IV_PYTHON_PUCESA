from funciones import registrar_estudiante, agregar_nota_estudiante, mostrar_estudiante, mostrar_todos

def menu():
    while True:
        print("----- SISTEMA DE REGISTRO DE ESTUDIANTES -----")
        print("1. Registrar nuevo estudiante")
        print("2. Agregar nota a un estudiante")
        print("3. Mostrar datos de un estudiante")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            agregar_nota_estudiante()
        elif opcion == "3":
            mostrar_estudiante()
        elif opcion == "4":
            mostrar_todos()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Ejecutar menú
if __name__ == "__main__":
    menu()
