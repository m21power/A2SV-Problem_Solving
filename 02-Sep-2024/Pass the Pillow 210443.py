# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        plus = True
        n = n-1
        while time >  n:
            time -= n
            plus = False if plus else True
        return (n+1) - time if not plus else 1 + time
        