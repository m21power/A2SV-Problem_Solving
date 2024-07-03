# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/

class Solution:
    def check(self,input):
        stack = []
        for symb in input:
            if symb == '(':
                stack.append('(')
                continue
            if stack:
                stack.pop()
            else:
                return False
        return True if not stack else False
    def generateParenthesis(self, n: int) -> List[str]:
        symbol = ['(',')']
        ans = set()
        def backtrack(cnt,pack):
            if cnt == n+n:
                if self.check(pack):
                    ans.add(''.join(pack))
                return
            for symb in symbol:
                pack.append(symb)
                backtrack(cnt + 1,pack)
                pack.pop()
        backtrack(0,[])
        return list(ans)


