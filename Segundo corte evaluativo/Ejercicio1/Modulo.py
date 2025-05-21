# Función que invierte las palabras de una frase usando una pila
def invertir_frase(frase):
    pila = []
    palabras = frase.split() # Divide la frase en palabras

    # Apila cada palabra
    for palabra in palabras:
        pila.append(palabra)

    frase_invertida = []
    # Desapila las palabras para invertir el orden
    while pila:
        frase_invertida.append(pila.pop())
        
    # Une las palabras invertidas en una nueva frase
    return ' '.join(frase_invertida)


