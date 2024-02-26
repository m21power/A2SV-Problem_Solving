class RecentCounter:

    def __init__(self):
        self.que=[]

    def ping(self, t: int) -> int:
        while len(self.que) and t-self.que[0]>3000:
            self.que.pop(0)
        self.que.append(t)
        return len(self.que)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)