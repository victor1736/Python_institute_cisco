'''
¿Cuál es la salida del siguiente fragmento de código?

R//["A", "B", "C"]

'''
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)