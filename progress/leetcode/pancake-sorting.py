class Solution:
    
    def pancakeSort(self, arr):
        def findMax(arr,n):
            m=0
            for i in range(n):
                if arr[i]>arr[m]:
                    m=i
            return m
        def flip(arr,i):
            j=0
            while j<i:
                
                arr[i],arr[j]=arr[j],arr[i]
                i-=1
                j+=1
        cur=len(arr)
        lis=[]
        while cur>1:
            m=findMax(arr,cur)
            if m==cur-1:
                cur-=1
            else:
                if m==0:
                    lis.append(cur)
                    flip(arr,cur-1)
                    cur-=1
                else:
                    lis.append(m+1)
                    flip(arr,m)

        return lis