# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        que = [root]
        while que:
            level = []
            for _ in range(len(que)):
                node = que.pop(0)
                if node:
                    que.append(node.left)
                    que.append(node.right)
                if node:
                    level.append(node.val)
                else:
                    level.append('null')
            for i in range(len(level)-1,-1,-1):
                if level[i] != "null":
                    ans.append(level[i])
                    break
        return ans      