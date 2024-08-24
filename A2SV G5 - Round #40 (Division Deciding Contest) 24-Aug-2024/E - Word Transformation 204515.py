# Problem: E - Word Transformation - https://codeforces.com/gym/543431/problem/E

from collections import Counter
from sys import stdin


def input(): return stdin.readline().strip()

T = int(input())

for _ in range(T):
    s, t = input().split()
    s_cnt = Counter(s)
    t_cnt = Counter(t)

    remove_cnt = {}
    ok = True
    for ch in s_cnt:
        remove_cnt[ch] = s_cnt[ch] - t_cnt[ch]
        if remove_cnt[ch] < 0:
            ok = False
    
    if not ok:
        print("NO")
        continue
    
    new_s = []
    for ch in s:
        if remove_cnt[ch] > 0:
            remove_cnt[ch] -= 1
        else:
            new_s.append(ch)
    
    if "".join(new_s) == t:
        print("YES")
    else:
        print("NO")