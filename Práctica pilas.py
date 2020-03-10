# Se importan los módulos de pila y conversión a postfija
from array_stack import ArrayStack as Stack
from infixPosfix import infixToPostfix

# Se introduce cualquier expresión que sea CORRECTA, y cada caracter separado por un espacio
expr = input("Introduce una expresión (con espacio entre caracteres): ")
# Se crea una lista con los símbolos para poder recorrerla en la función
opdor = ['*','/','-','+','(',')']

# Se convierte la expresión introducida en una lista para poder recorrerla elemento a elemento
expr.split()

# Se crea una variable con una cadena vacía para poder ignorarla con un comparador lógico dentro de la función
vacio = " "

while True:
    try:
        

for i in expr:
    if i == "(":
        
        

# Se crea una variable la cual, mediante la función de cambio a postfija, transforme la expresión infija introducida previamente
post = infixToPostfix(expr)

# Se declara la función
def evalInPos(post):
    # Se crea una variable que sea una pila vacía (con la clase 'ArrayStack' importada)
    op = Stack()
    # Se convierte la expresión postfija en una lista para poder recorrerla elemento a elemento
    post.split()
    # Se inicia un bucle for, el cual recorra la lista de la expresión postfija
    for token in post:
        # Se inserta una condición en la cual si el elemento no es vacío, y no es un operador, se almacene en una variable en la cual se convierta a entero, y se guarde en la pila de operandos
        if token is not vacio:
            if token not in opdor:
                opToken = float(token)
                op.push(opToken)
            # En este caso, si es un operador, se almacenan dos variables en las cuales, el último elemento introducido la pila de operandos será el segundo en operarse, y el penúltimo elemento será el primero en hacerlo
            elif token in opdor:
                segundo = op.pop()
                primero = op.pop()
                # Se establecen condiciones para saber qué operador se está leyendo, y se ejecuta la operación correspondiente
                if token == "*":
                    result = primero*segundo
                elif token == "/":
                    result = primero/segundo
                elif token == "-":
                    result = primero - segundo
                elif token == "+":
                    result = primero + segundo
                # El resultado de la operación se añade en el tope de la pila
                op.push(result)
    # La función devuelve el último elemento que quede en la pila despues de iterar todas las veces y realizar todas las operaciones,
    # y este será el resultado final de la expresión        
    return op.pop()



# Imprimo la expresión de ambas maneras y el resultado final de operarla
print("________________________________________________________________________")
print("\nLa expresión infija es: ", expr)
print("\nLa expresión posfija es: ", post)
print("\nEl resultado de la expresión es: ",(evalInPos(post)))
