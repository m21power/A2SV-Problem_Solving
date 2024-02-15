class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s==" ":
            return 0
        stack=[]
        c=0
        for i in s:
            if i=='(':
                stack.append('(')
            else:
                if len(stack)!=0:
                    stack.pop()
                else:
                    c+=1
        
        return len(stack)+c

        