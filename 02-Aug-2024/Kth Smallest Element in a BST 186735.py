# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack=[]
    def traverse(self,root):
        if root:
            self.traverse(root.left)
            self.stack.append(root.val)
            self.traverse(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root)
        return self.stack[k-1]