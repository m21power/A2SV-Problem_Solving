# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node,iter):
            if not iter:
                return True
            if not node:
                return False
            if node.val == iter.val:
                if dfs(node.left,iter.next) or dfs(node.right,iter.next):
                    return True 
            return False 
        if not head:
            return True
        if not root:
            return False 
        return dfs(root,head) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
            

        