# Problem: B - Grid Path - https://codeforces.com/gym/524965/problem/B

t = int(input()) 


for _ in range(t): 


    r, c , k = map(int, input().split())
    

    curr = 0

    for i in range(c-1): 
        curr += 1

    for i in range(r-1): 
        curr += c
    

    if curr == k: 
        print("YES")
    else:
        print("NO")