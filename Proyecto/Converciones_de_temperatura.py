from xdrlib import ConversionError
from Operaciones_basicas import Suma,Resta,Divicion,Multiplicacion

def Grados_kelvin(Grados):
    Resultado = Suma(Grados,273.15)
    return (Resultado)

def Grados_Fahrenheit(Grados):
    Resultado = Suma(Multiplicacion(Grados,Divicion(9,5)), 32)
    return (Resultado)

def Kelvin_Grados(Kelvin):
    Resultado =  Resta(Kelvin,273.15)
    return (Resultado)

def Kelvin_Fahrenheit(Kelvin):
    Resultado = Suma(Multiplicacion(Resta(Kelvin,273.15),Divicion(9/5)),32)
    return (Resultado)

def Fahrenheit_Grados(Fahrenheit):
    Resultado = Multiplicacion(Resta(Fahrenheit,32),Divicion(5,9))
    return (Resultado)

def Fahrenheit_Kelvin(Fahrenheit):
    Resultado = Suma(Multiplicacion(Resta(Fahrenheit,32),Divicion(5,9)),273.15)
    return (Resultado)


if __name__=="__main__":
    Convercion = ('Grados', 'Kelvin', 'Fahrenheit')
    print('Ingrese la escala de temperatura que va a suministrar de la siguiente tupla ',Convercion )
    Escala = input(':')
    print('Ingrese la escala de temperatura a la cual la desea convertir de la siguiente tupla ', Convercion)
    igualdad = input(':') 
    if Escala in Convercion and igualdad in Convercion:
        if Escala == Convercion[0]:
            if igualdad == Convercion[1]:
                Grados = float(input('Ingrese la temperatura: '))
                Resultado = Grados_kelvin(Grados)
                print('Usted introdujo: ', Grados , Escala , 'El cual corresponde a: ', Resultado, igualdad)
            if igualdad == Convercion[2]:
                Grados = float(input('Ingrese la temperatura: '))
                Resultado = Grados_Fahrenheit(Grados)
                print('Usted introdujo: ',Grados, Escala,'El cual corresponde a: ',Resultado, igualdad )
        if Escala == Convercion[1]:
            if igualdad == Convercion[0]:
                Kelvin = float(input('Ingrese la temperatura: '))
                Resultado = Kelvin_Grados(Kelvin)
                print('Usted introdujo: ',Kelvin, Escala,'El cual corresponde a: ',Resultado, igualdad)
            if igualdad == Convercion[2]:
                Kelvin = float(input('Ingrese la temperatura: '))
                Resultado = Kelvin_Fahrenheit(Kelvin)
                print('Usted introdujo: ',Kelvin, Escala,'El cual corresponde a: ',Resultado, igualdad)
    
        if Escala == Convercion[2]:
            if igualdad == Convercion[0]:
                Fahrenheit = float(input('Ingrese la temperatura: '))
                Resultado = Kelvin_Grados(Fahrenheit)
                print('Usted introdujo: ',Fahrenheit, Escala,'El cual corresponde a: ',Resultado, igualdad)
            if igualdad == Convercion[1]:
                Fahrenheit = float(input('Ingrese la temperatura: '))
                Resultado = Kelvin_Fahrenheit(Fahrenheit)
                print('Usted introdujo: ',Fahrenheit, Escala,'El cual corresponde a: ',Resultado, igualdad)
    else:
        print('Escala de temperatura Desconocida')