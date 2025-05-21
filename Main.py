from Modulos import ListaReproduccion

def menu():
    lista = ListaReproduccion()

    while True:
        print("\n--- Menú de Reproducción ---")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente canción")
        print("4. Reproducir canción anterior")
        print("5. Mostrar lista de reproducción")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Título de la canción: ")
            if lista.agregar_cancion(titulo):
                print("Canción agregada.")
            else:
                print("No se pudo agregar la canción (puede que ya exista).")

        elif opcion == '2':
            titulo = input("Título de la canción a eliminar: ")
            if lista.eliminar_cancion(titulo):
                print("Canción eliminada.")
            else:
                print("Canción no encontrada.")

        elif opcion == '3':
            siguiente = lista.reproducir_siguiente()
            if siguiente:
                print(f"Reproduciendo: {siguiente}")
            else:
                print("No hay siguiente canción.")

        elif opcion == '4':
            anterior = lista.reproducir_anterior()
            if anterior:
                print(f"Reproduciendo: {anterior}")
            else:
                print("No hay canción anterior.")

        elif opcion == '5':
            canciones = lista.mostrar_lista()
            if canciones:
                print("Lista de Reproducción:")
                for idx, titulo in enumerate(canciones, 1):
                    print(f"{idx}. {titulo}")
            else:
                print("La lista está vacía.")

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
