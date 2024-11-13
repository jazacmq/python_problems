from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        no_comun = []
        for palabra in words:
            for p in palabra:
                if p not in allowed:
                    no_comun.append(palabra)
                    break  # Si se encuentra una letra no permitida, se rompe el bucle interno

        # Filtrar las palabras que no están en no_comun
        r = [elemento for elemento in words if elemento not in no_comun]
        result = len(r)
        return result

# Pedir al usuario la entrada
allowed = input("Escribe los caracteres permitidos: ")
palabras = input("Lista de palabras separadas por espacios: ")
words = palabras.split()

# Crear una instancia de Solution y llamar al método
sol = Solution()
respuesta = sol.countConsistentStrings(allowed, words)
print("Número de palabras consistentes:", respuesta)