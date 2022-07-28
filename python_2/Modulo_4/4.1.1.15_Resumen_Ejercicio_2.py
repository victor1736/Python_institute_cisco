'''
Escribe una función lambda, estableciendo 
a 1 su argumento entero, y aplícalo a la función map() para producir la cadena 1 3 3 5 en la consola.
'''
any_list = [1, 2, 3, 4]
even_list = list(map(lambda n: n | 1, any_list)) 
print(even_list)