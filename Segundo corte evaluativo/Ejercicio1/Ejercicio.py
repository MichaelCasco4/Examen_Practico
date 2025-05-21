#Ejercicio #1: Inversión de palabras en una frase. Desarrolle un programa que 
#utilice una pila para invertir el orden de las palabras en una frase dada. Por ejemplo, 
#la frase "Hola mundo desde UAM" debería invertirse a "UAM desde mundo Hola". 

from Modulo import invertir_frase

def menu():
    while True:
        print("\n--- MENÚ: Inversión de palabras ---")
        print("1. Ingresar una frase para invertir")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            frase = input("Ingrese una frase: ")
            resultado = invertir_frase(frase)
            print("Frase invertida:", resultado)
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú si el archivo se corre directamente
if __name__ == "__main__":
    menu()
