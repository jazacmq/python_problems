from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        frecuencia={}
        resultado=[]
        palabras1=s1.split(" ")
        palabras2=s2.split(" ")
        palabras=palabras1+palabras2
        for s in palabras:
            if s in frecuencia:
                frecuencia[s]+=1
            else:
                frecuencia[s]=1
        for palabra,valor in frecuencia.items():
            if valor==1:
                resultado.append(palabra)
        return(resultado)
s1="esta manzana es grande"
s2="esta manzana es pequeña"
solution=Solution()
resultado=solution.uncommonFromSentences(s1,s2)
print(resultado)