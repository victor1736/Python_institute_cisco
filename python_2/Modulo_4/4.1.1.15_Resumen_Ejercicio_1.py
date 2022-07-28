'''
¿Cuál es el resultado esperado del siguiente código?

R// a e io u y

'''
class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  # Sí, sabemos que y no siempre se considera una vocal.
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]


vowels = Vowels()
for v in vowels:
    print(v, end=' ')