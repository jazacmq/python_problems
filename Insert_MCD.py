from typing import List,Optional



class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head=None

class Solution:
    def InsertMCD(self,head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current and current.next:
            #creamos un nuevo nodo
            for i in range (1,current.val+1):
                a=current.val%i
                b=current.next.val%i
                if a==0 and b==0:
                    new_data= i
            new_node=ListNode(new_data)
            #enlazamos el nodo con el siguiente.
            new_node.next=current.next
            current.next=new_node

            #movemos current dos hacia adelante.
            current=new_node.next

        return head

def printList(head: Optional[ListNode]):
    elements=[]
    current=head
    while current:
        elements.append(current.val)
        current=current.next
    print(elements)

head = ListNode(16)
head.next = ListNode(16)
head.next.next=ListNode(180)
head.next.next.next=ListNode(28)
head.next.next.next.next=ListNode(45)
head.next.next.next.next.next=ListNode(3)

solution=Solution()
print("lista original")
printList(head)

head = solution.InsertMCD(head)

print("Lista después de insertar elementos:")
printList(head)
