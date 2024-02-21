class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        sum=0
        print(costs)
        for i in costs:
            sum+=i
            if sum <= coins:
                count+=1
            if sum>coins:
                break
        return count

        