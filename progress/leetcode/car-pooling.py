class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        i=1
        while i<len(trips):
            j=i
            while j>0 and trips[j][1]<trips[j-1][1]:
                trips[j],trips[j-1]=trips[j-1],trips[j]
                j-=1
            i+=1
        heap = []
        cur_capacity = 0

        for npass, start, end in trips:
            
            while heap and heap[0][0] <= start:
                cur_capacity -= heap[0][1]
                heapq.heappop(heap)
            
           
            cur_capacity += npass
            if cur_capacity > capacity:
                return False
            
            
            heapq.heappush(heap, (end, npass))
        
        return True