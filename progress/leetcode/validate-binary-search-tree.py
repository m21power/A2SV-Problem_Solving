# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pv = None
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Check left and right subtrees
        if not self.isValidBST(root.left):
            return False
        if self.pv is not None and self.pv >= root.val:
            return False
        self.pv = root.val
        return self.isValidBST(root.right)
