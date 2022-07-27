'''
Ahora vamos a colocar la clase Point (ver Lab 3.4.1.14) dentro de otra clase. Además, vamos a poner tres 
puntos en una clase, lo que nos permitirá definir un triángulo.¿Cómo podemos hacerlo?

La nueva clase se llamará Triangle y esto es lo que queremos:

El constructor acepta tres argumentos - todos ellos son objetos de la clase Point.
Los puntos se almacenan dentro del objeto como una lista privada
La clase proporciona un método sin parámetros llamado perimeter(), que calcula el perímetro del triángulo descrito por 
los tres puntos; el perímetro es la suma de todas las longitudes de los lados (lo mencionamos para que conste, aunque 
estamos seguros de que tú mismo lo conoces perfectamente).
Completa la plantilla que te proporcionamos en el editor, ejecuta tu código y verifica si tu salida se ve igual que la 
nuestra.

A continuación puedes copiar el código de la clase Point, el cual se utilizo en el laboratorio anterior:
'''
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distance_from_xy(self, x, y):
        return math.sqrt((self.x-x)**2+ (self.y-y)**2)

    def distance_from_point(self, point):
        return math.sqrt((self.y-point.y)**2 + (self.x-point.x)**2)
class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.a = vertice1
        self.b = vertice2
        self.c = vertice3

    def perimeter(self):
        return (\
        self.a.distance_from_point(self.b)+\
        self.b.distance_from_point(self.c)+\
        self.a.distance_from_point(self.c) )   


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
