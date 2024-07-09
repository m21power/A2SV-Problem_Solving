# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i,n in enumerate(stones):
            stones[i] = -1 * n
        heapq.heapify(stones)
        i = 0
        while len(stones) >= 2:
            first ,second = heapq.heappop(stones),heapq.heappop(stones)
            if first == second:
                pass
            else:
                first,second = abs(first),abs(second)
                heapq.heappush(stones,-1 * abs(first-second))
        if len(stones) == 1: return abs(stones[0])
        return 0
        