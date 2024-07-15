# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        valueGraph = defaultdict(int)
        for i,lis in enumerate(equations):
            frm,to = lis
            graph[frm].append(to)
            graph[to].append(frm)
            valueGraph[(frm,to)] = values[i]
            valueGraph[(to,frm)] = 1/values[i]
        print(graph)
        print(valueGraph)
        def dfs(frm,to):
            if frm not in graph or to not in graph: return 0
            if frm == to :
                return 1
            ans = 0
            visited.add(frm)
            for t in graph[frm]:
                if t not in visited:
                    ans = valueGraph[(frm,t)] * dfs(t,to)
                    if ans: return ans
            return ans
        res = []
        for que in queries:
            frm,to = que
            visited = set()
            temp = dfs(frm,to)
            if temp: 
                res.append(temp)
            else:
                res.append(-1)
        return res



   