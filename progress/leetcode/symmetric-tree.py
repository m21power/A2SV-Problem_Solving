# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lis=[]
        que=[root]
        while que:
            level=[]
            for i in range(len(que)):
                node=que.pop(0)
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
                else:
                    level.append(None)
            if level:
                lis.append(level)
        lis.pop()
        for l in lis:
            i=0
            j=len(l)-1
            if i==j:
                pass
            else:
                while j>=i+1:
                    if l[i]!=l[j]:
                        return False
                    i+=1
                    j-=1
        return True
            
        