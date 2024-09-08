# Problem: A - Balanced Alphabet - https://codeforces.com/gym/519135/problem/A

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    
    numbers = n // k
    
    remaining = n % k
    
    ans = ""
    
    for i in range(k):
        ans += chr(i + ord("a")) * numbers
    ans += "a" * remaining
    print(ans)