# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/520688/problem/B

class UnionFind:
    def __init__(self, size) -> None:
        self.parent = [i for i in range(size)]
        self.size = [1 for i in range(size)]
 
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
 
        return self.parent[x]
 
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
 
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                rootx, rooty = rooty, rootx
 
            self.parent[rootx] = rooty
            self.size[rooty] += self.size[rootx]
 
    def connected(self, x, y):
        return self.find(x) == self.find(y)

n=int(input())
lst=list(map(int,input().split()))
from collections import defaultdict
graph=UnionFind(n)
for i in range(1,n+1):
    graph.union(i-1,lst[i-1]-1)
        
for i in range(n):
    graph.find(i)
print(len(set(graph.parent)))