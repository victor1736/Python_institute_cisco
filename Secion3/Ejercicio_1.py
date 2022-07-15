'''
¿Cuál es la salida del siguiente fragmento de código?

R// [6, 2, 3, 4, 5, 1]
'''

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)