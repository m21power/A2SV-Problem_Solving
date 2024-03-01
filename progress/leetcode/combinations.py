class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(comb,start):
            if len(comb)==k:
                res.append(comb[:]) # or u can use comb.copy
                return
            for i in range(start,n+1):
                comb.append(i)
                backtrack(comb,i+1)
                comb.pop()
        backtrack([],1) 
        return res     
        """
        res=[]
        state=[]
        def com(i):
            if len(state)==k:
                res.append(state[:])
                return
            if i>n:
                return 
            state.append(i)
            com(i+1)
            state.pop()
            com(i+1)
        com(1)
        return res"""