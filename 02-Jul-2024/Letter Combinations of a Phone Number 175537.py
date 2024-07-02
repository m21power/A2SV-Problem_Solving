# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digit = []
        dic = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        for dig in digits:
            digit.append(dic[int(dig)])
        ans = []
        def backtrack(i,pack):
            if i == len(digit):
                ans.append(''.join(pack))
                return
            for letter in digit[i]:
                pack.append(letter)
                backtrack(i+1,pack)
                pack.pop()
            return
        backtrack(0,[])
        return ans

            