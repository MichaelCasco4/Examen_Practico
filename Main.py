from Modulos import ColaPrioridad

def menu():
    cola = ColaPrioridad()

    while True:
        print("\n--- MENU ---")
        print("1. Insertar elemento")
        print("2. Eliminar elemento de mayor prioridad")
        print("3. Imprimir cola")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del elemento: ")
            try:
                prioridad = int(input("Ingrese la prioridad (Un número menor indica mayor prioridad): "))
                if prioridad < 1 or prioridad > 5:
                    print("Prioridad fuera de rango. Debe estar entre 1 (alta) y 5 (baja).")
                else:
                    cola.Insertar(nombre, prioridad)
            except ValueError:
                print("Prioridad inválida. Debe ser un número entero.")

        elif opcion == "2":
            cola.Eliminar()

        elif opcion == "3":
            cola.Imprimir()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
