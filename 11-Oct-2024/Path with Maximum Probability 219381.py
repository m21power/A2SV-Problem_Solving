# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        prob = defaultdict(int)
        ans = {i:0 for i in range(n)}
        for i,temp in enumerate(edges):
            graph[temp[0]].append(temp[1])
            graph[temp[1]].append(temp[0])
            prob[(temp[0],temp[1])] = succProb[i]
            prob[(temp[1],temp[0])] = succProb[i]
        heap = [(1,start)]
        visited = set()
        while heap:
            p,node = heappop(heap)
            p = abs(p)
            for nod in graph[node]:
                if (node, nod) not in visited:
                    ans[nod] = max(ans[nod],prob[(node,nod)] * p)
                    heappush(heap,((-1 * prob[(node,nod)] * p),nod))
                    visited.add((node,nod))
        return ans[end]