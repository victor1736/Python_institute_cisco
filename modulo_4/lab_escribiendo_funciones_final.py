'''
Tu tarea es escribir y probar una función que toma tres argumentos 
(un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si
cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código.
Esta prueba es solo el comienzo.
'''
def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    if month in (1, 3, 7, 8, 10, 12):
        return 31
    if month == 2:
        if is_year_leap(year) == True:
            return 29
        else:
            return 28
    else:
        return 30

def day_of_year(year, month, day):
#
# Escribe tu código nuevo aquí.
#

print(day_of_year(2000, 12, 31))

