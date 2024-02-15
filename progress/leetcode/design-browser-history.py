"""USING STACK"""
"""class BrowserHistory:

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
        """
class Node:
  def __init__(self, url: str):
    self.prev = None
    self.next = None
    self.url = url


class BrowserHistory:
  def __init__(self, homepage: str):
    self.curr = Node(homepage)

  def visit(self, url: str) -> None:
    new_node=Node(url)
    self.curr.next = new_node
    self.curr.next.prev = self.curr
    self.curr = new_node
    """the head continued changing within the current position if u try to access
    the current position of the vist it shows you the last value of the visit thats how the above
    algorithm works"""
  def back(self, steps: int) -> str:
    while self.curr.prev and steps > 0:
      self.curr = self.curr.prev
      steps -= 1
    return self.curr.url

  def forward(self, steps: int) -> str:
    while self.curr.next and steps > 0:
      self.curr = self.curr.next
      steps -= 1
    return self.curr.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)