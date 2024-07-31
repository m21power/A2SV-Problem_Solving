# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruit: List[int]) -> int:
        ans = 0
        left,right = 0,0
        dic = defaultdict(int)
        temp = 0
        while right < len(fruit):
            dic[fruit[right]] += 1
            while left < right and len(dic) > 2:
                dic[fruit[left]] -= 1
                if dic[fruit[left]] == 0:
                    dic.pop(fruit[left])
                left += 1
            ans = max(ans,(right - left + 1))
            right += 1
        return ans

        