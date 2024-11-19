
class Solution:
    def RemoveElements(self,val:int,nums:list[int])->int:
        y=0
        x=len(nums)
        for num in nums[:]:
            if num==val:    
                y+=1 
                nums.remove(val)
        k=x-y
        return(k)
nums = list(map(int, input("Anota los numeros: ").split()))
val = int(input("Valor a eliminar: "))

# Crea una instancia de Solution
solution = Solution()
k = solution.RemoveElements(val, nums)

print(f"Lista después de eliminar {val}: {nums}")
print(f"Cantidad de elementos restantes: {k}")