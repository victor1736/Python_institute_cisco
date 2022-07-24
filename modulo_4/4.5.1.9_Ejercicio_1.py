'''
¿Qué ocurrirá al intentar ejecutar el siguiente fragmento de código y por qué?

R// Entra a un bucle infinito

'''
def factorial(n):
    return n * factorial(n - 1)


print(factorial(4))