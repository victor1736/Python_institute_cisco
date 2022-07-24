'''
¿Cuál es el resultado esperado del siguiente código?

R//ValueError por que uno es '12.8' y el otro es '12'

'''
s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)