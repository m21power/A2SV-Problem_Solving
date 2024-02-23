# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack=[]
    def find(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.find(root.left)
            self.stack.append(root.val)
            self.find(root.right)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.find(root)
        s=[]
        flag=False
        
        for i in self.stack:
            if self.stack.count(i)>=2:
                flag=True
                if len(s)==0:
                    s.append(i)
                else:
                    if i not in s:
                        if self.stack.count(i)>self.stack.count(s[0]):
                            s.clear()
                            s.append(i)
                        elif self.stack.count(i)==self.stack.count(s[0]):
                            s.append(i)
                    else:
                        pass
        if flag:
            return s
        else:
            return self.stack
        