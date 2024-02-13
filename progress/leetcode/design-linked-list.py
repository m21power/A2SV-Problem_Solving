class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        

    def get(self, index: int) -> int:
        iter=self.head
        i=0
        while iter:
            if i==index:
                return iter.val
            iter=iter.next
            i+=1
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node

    def addAtTail(self, val: int) -> None:
        iter=self.head
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            return
        while iter.next:
            iter=iter.next
        iter.next=new_node

    def addAtIndex(self, index: int, val: int) -> None:
        iter=self.head
        i=0
        new_node=Node(val)
        if index==0:
            self.addAtHead(val)
            return
        while iter:
            if i+1==index:
                temp=iter.next
                iter.next=new_node
                new_node.next=temp
                return
            iter=iter.next
            i+=1
            
    def deleteAtIndex(self, index: int) -> None:
        iter=self.head
        i=0
        if index==0:
            self.head=iter.next
            return
        while iter:
            if i+1==index:
                if iter.next is None:
                    return
                iter.next=iter.next.next
                return
            iter=iter.next
            i+=1
       
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)