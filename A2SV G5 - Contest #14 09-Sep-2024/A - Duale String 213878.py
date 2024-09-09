# Problem: A - Duale String - https://codeforces.com/gym/520688/problem/A

for _ in range(int(input())):
    s=input()
    if len(s)%2==1 :
        print("NO")
    else:
        if(s[:len(s)//2]==s[len(s)//2:]):
            print("YES")
        else:
            print("NO")