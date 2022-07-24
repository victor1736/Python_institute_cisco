'''
¿Cuál es la salida del siguiente fragmento de código?

R//56

'''
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))