class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        m=skill[0]+skill[-1]
        p=skill[0]*skill[-1]
        sum=p
        i=1
        j=len(skill)-2
        while j>=i+1:
            if skill[i]+skill[j]==m:
                sum+=(skill[i]*skill[j])
                i+=1
                j-=1
            else:
                return -1
        return sum

        