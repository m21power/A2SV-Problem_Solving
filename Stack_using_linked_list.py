class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        iter=self.head
        while iter.next:
            iter=iter.next
        iter.next=new_node
        
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False    
    def pop(self):
        if Stack().is_empty():
            print("Oops! The stack is empty!")
            return 
        elif self.head.next is None:
            self.head=None
            return
        else:
            
            prev=None
            iter=self.head
            while iter.next:
                prev=iter
                iter=iter.next
            prev.next=None
    def peeking(self):
        iter=self.head
        while iter.next:
            iter=iter.next
        print(iter.data)


    def printing(self):
        cur=self.head
        while cur:
            print(cur.data,end=" ")
            cur=cur.next
