'''
¿Que ocurrirá cuando se ejecute el siguiente código? 

R// {"A": 1, "B": 2}
   
'''
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)
