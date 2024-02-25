# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        v1=p.val if p else None
        v2=q.val if q else None 
        if v1!=v2:
            return False
        return   ((self.isSameTree(p.left if p else None,q.left if q else None)) and
                 (self.isSameTree(p.right if p else None , q.right if q else None)))
    