from Modulos import Nodo, Lista_Enlazada

#Validacion de entrada en numero entero
def leer_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")

def main():
    lista = Lista_Enlazada()

    while True:

        print("------------MENU DE OPCIONES-------------")
        print("1. Insertar valor")
        print("2. Buscar valor")
        print("3. Mostrar lista")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = leer_entero("INGRESE EL VALOR A INSERTAR: ")  
            lista.insertar(valor)
            print("VALOR INSERTADO CORRECTAMENTE.")
        elif opcion == "2":
            valor = leer_entero("INGRESE EL VALOR A BUSCAR: ") 
            posicion = lista.buscar(valor)
            if posicion != -1:
                print(f"Valor encontrado en la posición {posicion}.")
            else:
                print("Valor no encontrado en la lista.")
        elif opcion == "3":
            lista.mostrar()
        elif opcion == "4":
            print("SALIENDO DEL PROGRAMA.....")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Llamamos a la función principal
if __name__ == "__main__":
    main()

