# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if root.val< p.val and root.val <q.val:
                return self.lowestCommonAncestor(root.right if root else None ,p,q)
            if root.val>p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left if root else None,p,q)
            if p.val <= root.val <=q.val:
                return root
            if q.val <= root.val <=p.val:
                return root