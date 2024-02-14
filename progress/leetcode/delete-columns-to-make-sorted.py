class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        #n=len(strs)
        count =0
        i=0
        while i <len(strs[0]):
            j=0
            flag=True
            while j<len(strs)-1:
                if strs[j][i]>strs[j+1][i]:
                    flag=False
                j+=1
            if flag==False:
                count+=1
            else:
                pass
            i+=1
        return count