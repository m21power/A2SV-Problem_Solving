class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        while i<= len(name) and j<len(typed):

            if i<len(name) and name[i]==typed[j]:
                i+=1
                j+=1
            elif i!=0 and name[i-1]==typed[j]:
                j+=1
            else:
                return False
        return i ==len(name) and j==len(typed)