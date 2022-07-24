'''
¿Cuál es la salida del siguiente fragmento de código?

R//
True
False
None

'''
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))