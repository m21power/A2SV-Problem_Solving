# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        def build_graph(node):
            if not node:
                return
            if node.left:
                graph[node.val].append([node.left.val,"L"])
                graph[node.left.val].append([node.val,"U"])
            if node.right:
                graph[node.val].append([node.right.val,"R"])
                graph[node.right.val].append([node.val,"U"])
            build_graph(node.left)
            build_graph(node.right)
        build_graph(root)

        self.ans = ""
        visited = set()
        def dfs(node,pack):
            if node == destValue:
                return ''.join(pack)
            visited.add(node)
            for nod,direc in graph[node]:
                if nod not in visited:
                    pack.append(direc)
                    temp = dfs(nod,pack)
                    pack.pop()
                    if not self.ans:
                        self.ans = temp
                    elif temp and len(self.ans) > len(temp):
                        self.ans = temp
            return self.ans
        return dfs(startValue,[])
