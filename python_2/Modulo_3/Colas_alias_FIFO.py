'''
Como ya sabes, una pila es una estructura de datos que realiza el modelo LIFO (último en entrar, primero en salir). Es fácil y 
ya te has acostumbrado a ello perfectamente.

Probemos algo nuevo ahora. Una cola (queue) es un modelo de datos caracterizado por el término FIFO: primero en entrar, primero
en salir. Nota: una cola (fila) regular que conozcas de las tiendas u oficinas de correos funciona exactamente de la misma manera:
un cliente que llegó primero también es el primero en ser atendido.

Tu tarea es implementar la clase Queue con dos operaciones básicas:

put(elemento), que coloca un elemento al final de la cola.
get(), que toma un elemento del principio de la cola y lo devuelve como resultado (la cola no puede estar vacía para realizarlo
correctamente).
Sigue las sugerencias:

Emplea una lista como tu almacenamiento (como lo hicimos con la pila).
put() debe agregar elementos al principio de la lista, mientras que get() debe eliminar los elementos del final de la lista.
Define una nueva excepción llamada QueueError (elige una excepción de la cual se derivará) y generala cuando get() intentes 
operar en una lista vacía.
Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si tu salida es similar a la nuestra.
'''
from xml.dom.minidom import Element


class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    pass
    #
    #  Escribe código aquí.
    #


class Queue:
    def __init__(self):
        self.Queue = []
        #
        # Escribe código aquí.
        #

    def put(self, elem):
        self.Queue.insert(0,elem)
        #
        # Escribe código aquí.
        #

    def get(self):
        if len(self.Queue)>0:
            elem=self.Queue[-1]
            del self.Queue[-1]
            return elem
        else:
            raise QueueError
        #
        # Escribe código aquí.
        #


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")