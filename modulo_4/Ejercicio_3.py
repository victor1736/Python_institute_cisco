'''
¿Cuál es la salida del siguiente fragmento de código?

R//[0, 2, 4,  6, 8, 10]

'''
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11))