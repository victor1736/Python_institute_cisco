'''
Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia.
Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de 
la revista Time de las 100 personas más influyentes del siglo XX.

a banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación 
de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).


Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

Paso 1: Crea una lista vacía llamada beatles.
Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista:
John Lennon, Paul McCartney y George Harrison.
Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista:
Stu Sutcliffe, y Pete Best.
Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
Por cierto, ¿eres fan de los Beatles? (Los Beatles son una de las bandas favoritas de Greg. Pero espera...¿Quién es Greg?)


'''
Beatles = []
print("Paso 1:", Beatles)

for i in range(0,3):
    ingreso = input('Ingresa el nombre del integrante de los Beatles: ')
    Beatles.append(ingreso)
print("Paso 2:", Beatles)

for i in range(2):
    ingreso = input('Ingresa el nombre del los integrantes de la bana que faltan: ')
    Beatles.append(ingreso)
print("Paso 3:", Beatles)

del Beatles[3]
del Beatles[4]
print("Paso 4:", Beatles)

ingreso = input('Ingresa el nombre de los integrantes que faltan: ')
Beatles.insert(0, ingreso)
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))