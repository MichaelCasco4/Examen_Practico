#Ejercicio #2: Verificación de paréntesis balanceados. Escriba un programa que 
#determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ] balanceados. 
#Use una pila para realizar el seguimiento de los paréntesis abiertos.

from Modulo2 import parentesis_balanceados

# Menú interactivo para verificar cadenas de paréntesis
def menu_verificacion_parentesis():
    while True:
        print("\n--- MENÚ: Verificación de paréntesis ---")
        print("1. Ingresar una cadena para verificar")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cadena = input("Ingrese una cadena con paréntesis: ")
            if parentesis_balanceados(cadena):
                print("Los paréntesis están balanceados.")
            else:
                print("Los paréntesis NO están balanceados.")
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el menú si el archivo se corre directamente
if __name__ == "__main__":
    menu_verificacion_parentesis()