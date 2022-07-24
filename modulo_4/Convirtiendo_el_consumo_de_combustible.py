'''
El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.

En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.

Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

Las funciones:

Se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente.
Toman un argumento (el valor correspondiente a sus nombres).
Complementa el código en el editor.

Ejecuta tu código y verifica si tu salida es la misma que la nuestra.

Aquí hay información para ayudarte:

1 milla = 1609.344 metros.
1 galón = 3.785411784 litros.
'''
def liters_100km_to_miles_gallon(liters):
    kms_per_mile = 1.609344
    liters_per_gallon = 3.785411784
    kms_per_liter = 100 / liters
    kms_per_gallon = kms_per_liter * liters_per_gallon
    miles_per_gallon = kms_per_gallon / kms_per_mile
    return miles_per_gallon
    
    

def miles_gallon_to_liters_100km(miles):
    kms_per_mile = 1.609344
    liters_per_gallon = 3.785411784
    gallon_per_100miles = 100 / miles
    gallon_per_100kms = gallon_per_100miles / kms_per_mile
    liters_per_100kms = gallon_per_100kms * liters_per_gallon
    return liters_per_100kms

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))