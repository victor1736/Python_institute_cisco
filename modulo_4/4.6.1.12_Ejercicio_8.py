'''
¿Cuál es la salida del siguiente programa?

R//
   blanco: (255, 255, 255),
   gris: (128, 128, 128),
   rojo: (255, 0, 0),
   verde: (0, 128, 0)

'''
colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)
