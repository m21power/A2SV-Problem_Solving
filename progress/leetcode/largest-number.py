class Solution:
    def largestNumber(self, num: List[int]) -> str:
        def compare(prev,nex):
            a=prev+nex
            b=nex+prev
            if int(a)>int(b)>0:
                return False
            else:
                return True

        for i,n in enumerate(num):
            num[i]=str(n)
        i=1
        while i<len(num):
            j=i
            while compare(num[j-1],num[j]) and j>=1:
                num[j-1],num[j]=num[j],num[j-1]
                j-=1
            i+=1
        a=''.join(num)
        c=0
        for i in a:
            if int(i)==0:
                c+=1
        if c==len(a):
            return '0'

        return ''.join(num)