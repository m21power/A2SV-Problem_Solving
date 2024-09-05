# Problem: E - Machine Testing - https://codeforces.com/gym/513152/problem/E

import sys
from math import ceil, inf
input = lambda : sys.stdin.readline().strip()


for t in range(int(input())):
    n = int(input())
    health = list(map(int, input().split()))
    power = list(map(int, input().split()))


    stack = [(inf, power[0])]
    ans = 0
    for i in range(1, n):
        duration = 0
        while health[i] - (stack[-1][0] - duration)*stack[-1][-1] > 0:
            t, p = stack.pop()


            health[i] -= (t-duration)*p
            duration += (t-duration)
       
        duration += ceil(health[i]/stack[-1][-1])
        stack.append((duration, power[i]))
        ans = max(ans, duration)
   
    print(ans)
