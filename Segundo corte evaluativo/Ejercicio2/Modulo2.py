# Función que verifica si los paréntesis están balanceados usando una pila
def parentesis_balanceados(cadena):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}  # Diccionario de paréntesis cerrados y su par abierto

    for caracter in cadena:
        if caracter in '([{':
            pila.append(caracter)  # Apila paréntesis abiertos
        elif caracter in ')]}':
            # Si la pila está vacía o no coincide el par, no está balanceado
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()  # Paréntesis correcto, desapilar

    # Si la pila está vacía al final, están balanceados
    return not pila