'''
¿Cuál es la salida del siguiente fragmento de código?

R//
2
3

'''
a = 1


def fun():
    global a
    a = 2
    print(a)


fun()
a = 3
print(a)