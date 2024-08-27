# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #it would be easy right if the question says it 
        #would start from the root node, so why u can't make everyone root.node, 
        #thats where self.pathSum(root.left) and self.pathSum(root.right) came from
        def dfs(node,target):
            if not node:
                return 0
            res = 0
            if target == node.val:
                res += 1
            res += dfs(node.left,target - node.val) + dfs(node.right,target - node.val)
            return res
        if not root: return 0
        return dfs(root,targetSum) + self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum)
        