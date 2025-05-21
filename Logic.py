from Pila import Pila

def es_operador(token):
    return token in '+-*/^'

def imprimir_pila_en_orden(pila):
    elementos = []
    while pila.no_vacia():
        elementos.append(pila.pop())
    resultado = ' '.join(str(dato) for dato in reversed(elementos))
    print(resultado)
    return resultado
    


def precedencia(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0

def es_izq_asociativo(op):
    return op != '^'  # ^ es asociativo a la derecha

def shunting_yard(expresion):
    salida = Pila()       # pila de salida
    operadores = Pila()   # pila de operadores

    simbolos = expresion.split()

    for simb in simbolos:
        if simb.isnumeric():
            salida.push(simb)
        elif simb == '(':
            operadores.push(simb)
        elif simb == ')':
            while operadores.no_vacia() and operadores.peek() != '(':
                salida.push(operadores.pop())
            operadores.pop()  # eliminar el paréntesis '('
        elif es_operador(simb):
            while (operadores.no_vacia() and es_operador(operadores.peek()) and
                   (precedencia(operadores.peek()) > precedencia(simb) or
                   (precedencia(operadores.peek()) == precedencia(simb) and es_izq_asociativo(simb)))):
                salida.push(operadores.pop())
            operadores.push(simb)

    while operadores.no_vacia():
        salida.push(operadores.pop())

    return salida

def evaluar_postfija(expresion):
    pila = Pila()
    simbolos = expresion.split()

    for simb in simbolos:
        if simb.isnumeric():
            pila.push(int(simb))
        elif es_operador(simb):
            b = pila.pop()
            a = pila.pop()
            if simb == '+':
                pila.push(a + b)
            elif simb == '-':
                pila.push(a - b)
            elif simb == '*':
                pila.push(a * b)
            elif simb == '/':
                pila.push(a / b)
            elif simb == '^':
                pila.push(a ** b)

    return pila

def expresiones(expresion):
    resultado = shunting_yard(expresion)
    resultadoCaracter = imprimir_pila_en_orden(resultado)
    evaluada = evaluar_postfija(resultadoCaracter)
    imprimir_pila_en_orden(evaluada)


print("Ejemplo de expresion 1")
expresion = "5 * 4 + ( 9 / 3 + 8 * 2 )"
expresiones(expresion)


print("Ejemplo de expresion 2")
expresion = "7 + 3 * ( 9 + 5 * 2 ^ 3 - 8 )"
expresiones(expresion)  

print("Ejemplo de expresion 3")
expresion = "4 * ( 2 + 3 - 2 ) * ( 4 + 8 - 5 ) "
expresiones(expresion)  

print("Ejemplo de expresion 4")
expresion = "8 + 4 + ( ( 5 ^ 2 + 6 ) * 4 )"
expresiones(expresion)  

print("Ejemplo de expresion 5")
expresion = "6 * 2 + 8 - 3 * 2 / 2"
expresiones(expresion)  