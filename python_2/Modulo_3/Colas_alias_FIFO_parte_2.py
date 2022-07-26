'''
Tu tarea es extender ligeramente las capacidades de la clase Queue. Queremos que tenga un método sin parámetros que devuelva True 
si la cola está vacía y False de lo contrario.

Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si genera un resultado similar al nuestro.

A continuación, puedes copiar el código que usamos en el laboratorio anterior:
'''
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.Queue = []
    def put(self, elem):
        self.Queue.insert(0,elem)
    def get(self):
        if len(self.Queue) >0:
            elem = self.Queue[-1]
            del self.Queue[-1]
            return elem
        else:
            raise QueueError
    #
    # Código del laboratorio anterior.
    #


class SuperQueue(Queue):
    def isempty(self):
        return len(self.Queue)== 0
    #
    # Escribe código nuevo aquí.
    #


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
