'''
Escenario
Imagina una lista: no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros.
Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.

Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista.
El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

Nota: Asume que la lista original está ya dentro del código, no tienes que ingresarla desde el teclado. 
Por supuesto, puedes mejorar el código y agregar una parte que pueda llevar a cabo una conversación con 
el usuario y obtener todos los datos.

Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal, no necesitas actualizar la lista actual.

No hemos proporcionado datos de prueba, ya que sería demasiado fácil. Puedes usar nuestro esqueleto en su lugar.

'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list_2 = []

for i in  my_list:
    if i not in my_list_2:
        my_list_2.append(i)
        

print("La lista con elementos únicos:")
print(my_list_2)
