# Problem: B - tourist orz! - https://codeforces.com/gym/522079/problem/B

t = int(input())
for _ in range(t):
    n, z = map(int, input().split())
    a = list(map(int, input().split()))

    max_val = 0
    for num in a:
        max_val = max(max_val, num | z)

    print(max_val)