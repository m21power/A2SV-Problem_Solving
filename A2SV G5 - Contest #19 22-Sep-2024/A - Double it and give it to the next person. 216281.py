# Problem: A - Double it and give it to the next person. - https://codeforces.com/gym/527294/problem/A

def fun(st):
    t = st[::-1]
    return st + t

for _ in range(int(input())):
    st = input()
    print(fun(st))