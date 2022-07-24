'''
¿Cuál es el resultado esperado del siguiente código?

R//ABC123xyz
la linea 9  pasa por todos los  atributos de la cadena
la linea 10 identifica los atributos que son mayusculas en la cadena y la 11 los combierte en minuscula la siguiente linea hace lo contrario e imprime

'''
for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')