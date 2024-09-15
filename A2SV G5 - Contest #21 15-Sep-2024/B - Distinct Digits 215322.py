# Problem: B - Distinct Digits - https://codeforces.com/gym/530187/problem/B

for _ in range(int(input())):
    n = int(input())

    ans = []
    for digit in range(9, 0, -1):
        if n >= digit:
            ans.append(digit)
            n -= digit
    ans.reverse()
    print(*ans, sep="")