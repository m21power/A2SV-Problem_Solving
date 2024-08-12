# Problem: B - Optimal Point - https://codeforces.com/gym/535749/problem/B

for _ in range(int(input())):
    N, K = map(int, input().split())
    
    l_ok = r_ok = False
    for _ in range(N):
        l, r = map(int, input().split())
        
        if l == K:
            l_ok = True
        if r == K:
            r_ok = True
    
    if l_ok and r_ok:
        print("YES")
    else:
        print("NO")