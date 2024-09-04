# Problem: C - Spaceship Attack - https://codeforces.com/gym/511242/problem/C

from bisect import bisect_right
from sys import stdin


def input(): return stdin.readline()[:-1]


S, B = map(int, input().split())
a = list(map(int, input().split()))
dg = []
for _ in range(B):
    d, g = map(int, input().split())
    dg.append((d, g))

dg.sort()
pref_sum = [0]
cur_sum = 0
ds = []
for d, g in dg:
    ds.append(d)
    cur_sum += g
    pref_sum.append(cur_sum)

ans = []
for ai in a:
    idx = bisect_right(ds, ai)
    ans.append(pref_sum[idx])
print(*ans)