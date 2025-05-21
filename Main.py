from Modulos import Elementos, ColaPrioridad

# Validación de entrada para prioridad
def leer_entero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        
        except ValueError:
            print("Entrada Invalida, Debe de ser un numero entero.\n ")

def main():
    cola = ColaPrioridad()

    while True:

        print("-----------MENU DE PRIORIDADES------------")
        print("1. Encolar elemento")
        print("2. Desencolar elemento")
        print("3. Mostrar elementos en cola")
        print("4. SALIR")

        opcion = input("SELECCIONE UNA OPCION DEL MENU: ")

        if opcion == "1":

            nombre = input("Ingresa el nombre del elemento: ")
            prioridad = leer_entero("Ingrese la prioridad (menor es mas prioritario) ")
            cola.encolar(nombre,prioridad)
            print("ELEMENTO ENCOLADO EXITOSAMENTE")

        elif opcion == "2":

            elemento = cola.descolocar()
            if elemento:
                print(f"ELEMENTO DESENCOLADO: {elemento}")
            else:
                print("La cola esta vacia..")
        elif opcion == "3":
            cola.mostrar()
        
        elif opcion =="4":
            print("SALIENDO DEL PROGRAMA....")
            break

        else:
            print("Opción inválida. Inténtelo de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    main()





