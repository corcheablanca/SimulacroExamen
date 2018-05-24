#Escriba el codigo necesario para que al ejecutar
#python ejercicio1.py se impriman los enteros del 10 al 1 en cuenta regresiva.
import numpy as np
x = np.linspace(0,10,10)

for i in range(len(x)):
    s = x[9-i]
    print(s)