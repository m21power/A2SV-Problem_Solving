# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children # list of children which is node
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root :
            return []
        dummy = Node(None,[root])
        def dfs(node):
            if node.children:
                for nod in node.children:
                    dfs(nod)
                    ans.append(nod.val)
        dfs(dummy)
        return ans
        
        