# Problem: B - Mapping the Maze - https://codeforces.com/gym/515998/problem/B

from collections import Counter
n,k = list(map(int,input().split()))
degree = [0 for i in range(n)]
for i in range(k):
    x,y = list(map(int,input().split()))
    x -= 1
    y -= 1
    
    degree[x] += 1
    degree[y] += 1
 
count = Counter(degree)
 
if count[2] == n:
    print('ring topology')
elif count[1] == 2 and count[2] == (n - 2):
    print('bus topology')
elif count[1] == n - 1 and count[n - 1] == 1:
    print('star topology')
else:
    print("unknown topology")