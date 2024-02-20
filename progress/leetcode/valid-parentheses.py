class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        op=['(','[','{']
        cl=[')',']','}']
        dic={'(':')','[':']','{':'}'}

        for i in s:
            
            if i in op:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                else:
                    par=stack.pop()
                    if dic[par]==i:
                        continue
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
