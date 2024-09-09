# Problem: C - Balanced Parentheses Clusters - https://codeforces.com/gym/520688/problem/C

class UnionFind:
	def __init__(self, size):
    		self.parent = list(range(size))
    		self.rank = [0] * size

	def find(self, element):
            if self.parent[element] != element:
                    self.parent[element] = self.find(self.parent[element])
            return self.parent[element]

	def union(self, element_a, element_b):
            root_a, root_b = self.find(element_a), self.find(element_b)
            if root_a != root_b:
                if self.rank[root_a] > self.rank[root_b]:
                    self.parent[root_b] = root_a
                elif self.rank[root_a] < self.rank[root_b]:
                    self.parent[root_a] = root_b
                else:
                    self.parent[root_a] = root_b
                    self.rank[root_b] += 1

def solve():
	num_pairs = int(input())
	brackets = input().strip()
	uf = UnionFind(2 * num_pairs)
	stack = []
	for i, bracket in enumerate(brackets):
            if bracket == "(":
                    stack.append(i)
            else:
                top = stack.pop()
                uf.union(i, top)
                if i + 1 < 2 * num_pairs and brackets[i + 1] == "(":
                    uf.union(i, i + 1)
	num_connected_components = sum(1 for i, parent in enumerate(uf.parent) if i == parent)
	print(num_connected_components)

num_tests = int(input())
for _ in range(num_tests):
	solve()