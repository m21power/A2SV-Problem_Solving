# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch == 'D' or ch == 'C' or ch == '+':
                if ch =='C' and stack:
                    stack.pop()
                elif ch == 'D' and stack:
                    stack.append(2*stack[-1])
                else:
                    if len(stack) >= 2:
                        stack.append(stack[-1] + stack[-2])
                    else:
                        stack.append(stack[-1])
            else:
                stack.append(int(ch))
        return sum(stack)

        