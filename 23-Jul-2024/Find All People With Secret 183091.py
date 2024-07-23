# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class UnionFind:
    def __init__(self,n):
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.rank[0] = 2**31
    def find(self, x: int) -> int:
        if self.root[x] != x: 
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self,n1,n2):
        rootx,rooty = self.find(n1),self.find(n2)
        if rootx == rooty: return False

        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
        return True
    def isConnected(self,n1,n2):
        return self.find(n1) == self.find(n2)
    def reset(self,x):
        self.root[x] = x
        self.rank[x] = 1
class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int):
        g = defaultdict(list)
        for x, y, t in meetings: g[t].append((x, y))
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        for _, v in sorted(g.items()):
            for x, y in v: 
                uf.union(x, y)
            for x, y in v:
                if uf.isConnected(x, 0):
                    continue
                else:
                    # since it is uselesss if it is not connected with 0
                    uf.reset(x)
                    uf.reset(y)
        
        return [x for x in range(n) if uf.isConnected(x, 0)]
