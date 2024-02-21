class Solution:
    def check(self,pcount,scount):
        for let in pcount:
            if let not in scount:
                return False
            else:
                if pcount[let]!=scount[let]:
                    return False
                else:
                    pass
        return True
    def findAnagrams(self, s: str, p: str):
        pcount={}
        scount={}
        lis=[]
        for let in p:
            if let not in pcount:
                pcount[let]=p.count(let)
        for i,let in enumerate(s):
            if let in scount:
                scount[let]+=1
            else:
                scount[let]=1
            if i==len(p)-1:
                break
        if self.check(pcount,scount):
            lis.append(0)
        left=1
        while left<=len(s)-len(p):
            right=left+len(p)-1
            if scount[s[left-1]]==1:   
                scount.pop(s[left-1])
            else:
                scount[s[left-1]]-=1
            if s[right] in scount:
                scount[s[right]]+=1  
            else:
                scount[s[right]]=1
            if self.check(pcount,scount):
                lis.append(left)
            else:
                pass
            left+=1
            
        return lis