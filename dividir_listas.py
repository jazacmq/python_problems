#Dividir una lista en partes iguales priorizando los primeros elementos si es que no se puede en partes iguales


#definition for singly linked_list
from typing import Optional,List

class ListNode:
  def __init__(self,val=0,next=None):
          self.val=val
          self.next=next
class Solution:
    def splitListtoParts(self,head:Optional[ListNode],k:int) -> List[Optional[ListNode]]:
        current=head
        count=0
        while current:
            count+=1
            current=current.next
    #vamos a dividir la lista
        partes,extra=divmod(count,k)

        current=head
        result=[]
        for i in range(k):
            head_part=current
            for j in range(partes-1+(i<extra)):
                if current:
                    current=current.next
            if current:
                next_node=current.next
                current.next=None
                current=next_node
            result.append(head_part)
        return result

def create_linked_list(values):
    """Convierte una lista de valores en una lista enlazada y devuelve su cabeza."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """Imprime la lista enlazada desde el nodo head."""
    result = []
    while head:
        result.append(f"[{head.val}]")
        head = head.next
    print(",".join(result))

values = list(map(int, input("Introduce los valores de la lista enlazada separados por espacios: ").split()))
k = int(input("Introduce el número de partes en las que deseas dividir la lista: "))

# Crear la lista enlazada y llamar a la función
head = create_linked_list(values)
solution = Solution()
parts = solution.splitListtoParts(head, k)

print("\nLa lista dividida en partes:")
for i, part in enumerate(parts):
    print(f"Parte {i + 1}: ", end="")
    print_linked_list(part)

#Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
#Output: [[1,2,3,4],[5,6,7],[8,9,10]]
