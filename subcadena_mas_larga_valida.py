def LongestSubstring(s:str)->int:
        vocal_to_bit={'a':1,'e':2,'i':4,'o':8,'u':16}
        mask=0
        seen= {0:-1}
        #seen es un diccionario que guarda la primera vez que vemos cada máscara de bits.
        #Inicialmente, lo configuramos como {0: -1}
        max_length= 0

        for i, char in enumerate(s):
            if char in vocal_to_bit:
                mask^=vocal_to_bit[char]

            if mask in seen:
                max_length=max(max_length,i-seen[mask])
                #Cada vez que encontramos una máscara mask que ya apareció antes, 
                #significa que la subcadena entre las dos apariciones tiene todas las vocales en cantidades pares.
            else:
                seen[mask]= i

        return(max_length)

s = "eleetminicoworoep"
print(LongestSubstring(s))  # Salida esperada: 13