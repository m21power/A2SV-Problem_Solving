# Problem: Z-Sort - https://codeforces.com/problemset/problem/652/B

def fun(arr):
    i = 1
    while i < len(arr):
        if (i+1) % 2 == 0:
            if arr[i] < arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
        else:
            if arr[i] > arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
        i+=1
    return arr

n = int(input())
arr = list(map(int,input().split()))
for n in fun(arr):
    print(n,end = " ")
