# Problem: C - Painting Class - https://codeforces.com/gym/517685/problem/C

from collections import deque
from sys import stdin


def input(): return stdin.readline().strip()

N = int(input())

parents = list(map(int, input().split()))
color = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for ch, p in enumerate(parents, 1):
    adj[p - 1].append(ch)

q = deque([(0, color[0])])
ans = 1

while q:
    v, c = q.popleft()
    for ch in adj[v]:
        q.append((ch, color[ch]))
        ans += (color[ch] != c)
print(ans)