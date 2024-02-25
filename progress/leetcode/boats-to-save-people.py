class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        i=0
        j=len(people)-1
        while j>=i:
            remain=limit-people[j]
            j-=1
            if people[i]<=remain:
                i+=1
            count+=1
        return count