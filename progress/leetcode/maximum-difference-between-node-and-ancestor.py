# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi=0
    def dfs(self,root,cur_max,cur_min):
        if not root:
            return
        self.maxi=max(self.maxi,abs(cur_max-root.val),abs(cur_min-root.val))
        self.dfs(root.left,max(cur_max,root.val),min(cur_min,root.val))
        self.dfs(root.right,max(cur_max,root.val),min(cur_min,root.val))
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.dfs(root,root.val,root.val)
        return self.maxi
        