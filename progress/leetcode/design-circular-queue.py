class MyCircularQueue:

    def __init__(self, k: int):
        self.que=[]
        self.k=k
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.que.append(value)
            return True
    def deQueue(self) -> bool:
        if self.que:
            self.que.pop(0)
            return True
        else:
            return False
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.que[0]
    def Rear(self) -> int:
        if self.que:
            return self.que[-1]
        else:
            return -1
    def isEmpty(self) -> bool:
        if self.que:
            return False
        else:
            return True
    def isFull(self) -> bool:
        if len(self.que)==self.k:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()