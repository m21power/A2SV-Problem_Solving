# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diffp = list(zip(difficulty,profit))
        diffp.sort()
        prof = []
        prev = -1
        for diff,p in diffp:
            if p > prev:
                prof.append(p)
                prev = p
            else:
                prof.append(prev)
        def binary(num):
            left,right = 0,len(diffp)-1
            while left <= right:
                mid = (left + right) //2
                if diffp[mid][0] > num:
                    right = mid - 1
                elif diffp[mid][0] < num:
                    left = mid + 1
                else:
                    left = mid + 1
            return right
        res = 0
        for n in worker:
            indx = binary(n)
            if indx == -1:
                res += 0
            else:
                res += prof[indx]
        return res

        
        