#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n,ar):
    # Write your code here
    x=len(ar)
    frecuencia = {}
    y=0
    if n==x:
        # Recorrer cada elemento en el arreglo
        for numero in ar:
                # Si el número ya está en el diccionario, incrementar su valor en 1
            if numero in frecuencia:
                    frecuencia[numero] += 1

                # Si el número no está en el diccionario, agregarlo con un valor de 1
            else:
                    frecuencia[numero] = 1

        y=sum(valor for valor in frecuencia.values() if valor==2)
        a=sum((int(valor/2)) for valor in frecuencia.values()if valor%2==0 and valor>1)
        b=sum((int(valor/2)) for valor in frecuencia.values()if valor%2==1 and valor>1)
        total=a+b
        print(frecuencia.values())
        print(total)
    else:
         print("no es el tamaño")
        

n = int(input("cual es el tamaño del arreglo").strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)


