class Solution:
    @staticmethod
    def mergeArrays(m, n, nums1, nums2):
        cont1 = len(nums1)
        car1 = cont1 - m
        cont2 = len(nums2)
        car2 = cont2 - n

        if cont1 != m:
            del nums1[-car1:]  # Modifica nums1 en su lugar
        elif cont2 != n:
            del nums2[-car2:]  # Modifica nums2 en su lugar

        nums1.extend(nums2)
        nums1.sort()
        return nums1


# Entrada del usuario
m = int(input("Ingrese el valor de m: "))
n = int(input("Ingrese el valor de n: "))
nums1 = list(map(int, input("Ingrese los elementos de nums1 separados por espacios: ").split()))
nums2 = list(map(int, input("Ingrese los elementos de nums2 separados por espacios: ").split()))

# Llamada a la función de la clase
nums1 = Solution.mergeArrays(m, n, nums1, nums2)
print(nums1)
