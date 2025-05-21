from Pila import Pila

#Validar que sea un operador
def es_operador(simb):
    return simb in '+-*/^'

def imprimir_pila_en_orden(pila):
    elementos = []
    while pila.no_vacia():
        elementos.append(pila.pop())
    resultado = ' '.join(str(dato) for dato in reversed(elementos))
    print(resultado)
    return resultado

# Funcion para saber la precedencia de los operadores
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
        if simb.isnumeric(): # si es un número lo agregamos a la salida
            salida.push(simb)
        elif simb == '(': # si es un paréntesis izquierdo lo agregamos a la pila de operadores
            operadores.push(simb)
        elif simb == ')': # si es un paréntesis derecho, sacamos de la pila de operadores hasta encontrar el paréntesis izquierdo
            while operadores.no_vacia() and operadores.peek() != '(':
                salida.push(operadores.pop())
            operadores.pop()  # eliminar el paréntesis '('
        elif es_operador(simb): # si es un operador
            # mientras la pila de operadores no esté vacía y el operador en la cima de la pila tenga mayor o igual precedencia
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
        elif es_operador(simb): # si es un operador, sacamos los dos últimos números de la pila
            # y aplicamos la operación
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

def expresiones(expresion): # función para evaluar la expresión
    # Primero convertimos la expresión infija a postfija
    resultado = shunting_yard(expresion)
    #luego imprimimos la pila en orden y guardados el resultado
    resultadoCaracter = imprimir_pila_en_orden(resultado)
    # Finalmente evaluamos la expresión postfija
    evaluada = evaluar_postfija(resultadoCaracter)
    
    imprimir_pila_en_orden(evaluada) 

while True:
    expresion = input("Ingrese una expresión aritmética con espacio entre cada caracter (o escriba 'salir' para terminar): ")
    if expresion.lower() == 'salir':
        break
    expresiones(expresion)