from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        # Implementamos un algoritmo de ordenación (por ejemplo, Bubble Sort)
        # con nuestra propia lógica de comparación
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Comparamos las concatenaciones
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    # Intercambiamos si el orden no es el correcto
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        # Si el número más grande es "0", devolvemos "0"
        if nums[0] == "0":
            return "0"
        
        # Concatenamos los números ordenados
        return "".join(nums)
solution=Solution()
nums = [3, 30, 34, 5, 9]
largestNumber=solution.largestNumber(nums)
nums = [3, 30, 34, 5, 9]
print(largestNumber)  # Salida: "9534330