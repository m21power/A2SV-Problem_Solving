class Solution:
    def plusOne(self, l: List[int]) -> List[int]:
        l=list(map(str,l))
        li=[]
        l=''.join(l)
        l=int(l)+1
        for i in str(l):
            li.append(int(i))
        return li



        