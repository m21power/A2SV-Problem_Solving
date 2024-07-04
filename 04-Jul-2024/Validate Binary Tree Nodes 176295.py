# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class UnionFind:
    def __init__(self,n):
        self.par = {i:i for i in range(n)}
        self.rank = {i:1 for i in range(n)}
        self.taken = {i:False for i in range(n)}
    def find(self,num):
        if self.par[num] != num:
            self.par[num] = self.find(self.par[num])
            num = self.par[num]
        return self.par[num]
    def union(self,num1,num2):
        if self.taken[num1]: return False
        self.taken[num1] = True
        p1,p2 = self.find(num1),self.find(num2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UnionFind(n)
        for i in range(n):
            left,right = leftChild[i],rightChild[i]
            if left != -1:
                if not uf.union(left,i):
                    return False
            if right != -1:
                if not uf.union(right,i):
                    return False       
        m = 0
        print(uf.rank)
        for key,item in uf.rank.items():
            m = max(item,m)
        return True if m == n else False


