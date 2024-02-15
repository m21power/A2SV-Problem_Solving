class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[]
        self.visit(homepage)
        
    def visit(self, url: str) -> None:
        self.history.append(url)
        self.front=[]
        

    def back(self, steps: int) -> str:
        while len(self.history)>1 and steps>0:
            self.front.append(self.history.pop(-1))
            steps-=1
        return self.history[-1]

        

    def forward(self, steps: int) -> str:
        while self.front  and steps>0:
            self.history.append(self.front.pop(-1))
            steps-=1
        return self.history[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)