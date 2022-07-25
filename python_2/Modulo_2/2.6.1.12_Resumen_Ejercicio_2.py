'''
¿Cuál es el resultado esperado del siguiente código?

R//
cero 

'''
try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("cero")
except IndexingError:
    print("índice")
except:
    print("algo")