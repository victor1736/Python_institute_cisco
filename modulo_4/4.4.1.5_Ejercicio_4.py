'''
¿Cuál es la salida del siguiente fragmento de código?

R//
2
2

'''
a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
fun()
print(a)