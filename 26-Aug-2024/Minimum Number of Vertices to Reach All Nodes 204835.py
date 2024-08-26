# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [0]*n
        ans = []
        for frm,to in edges:
            incoming[to] += 1
        for i,n in enumerate(incoming):
            if not n:
                ans.append(i)
        return ans

        