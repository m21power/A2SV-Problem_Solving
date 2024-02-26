class Solution:
    def minimumSteps(self, s: str) -> int:
        one =0
        res=0
        for i in s:
            if i=='1':
                one+=1 #count number of 1 
            else:
                res+=one # since it the swaping should be next to each other
                        # when we get zero we increamenting our counter
        return res
