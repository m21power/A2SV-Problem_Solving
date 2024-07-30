# Problem: All Ancestors of a Node in a Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0] * n
        graph = defaultdict(list)
        res = [[] for _ in range(n)]
        for fr,to in edges:
            graph[fr].append(to)
            indegree[to] += 1
        que = []
        for i,n in enumerate(indegree):
            if n == 0:
                que.append(i)
        while que:
            for _ in range(len(que)):
                node = que.pop(0)
                for n in graph[node]:
                    temp = list(set(res[n] + res[node] + [node]))
                    res[n] = sorted(temp)
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        que.append(n)
        return res
