# programa N. 5. repeticiones: Programa que genere un numero aleatorio y que permita ingresar un numero para tratar de adivinarlo 

#input
from random import random
import random


n=int(input("Ingrese su numero: "))
a=random.randint(1,100)
#processing

while n!=a:
    if n>a:
        print("\nEl numero ingresado es mayor al que trata de adivinar, intente nuevamte ")
    else: 
        print("\nEl numero ingresado es menor al que trata de adivinar, intente nuevamente ")
    n=int(input("\nIngrese nuevamente el numero: "))
print("\nAdivino, el numero es: "+str(n))