# Problem: A - Distribute - https://codeforces.com/gym/524965/problem/A

n = int(input())
 
nums = list(map(int, input().split()))
 
 
for i in range(n): 
    nums[i] = [nums[i], i+1]
#print(nums)
nums.sort()
l = 0 
r = n - 1
 
while l < r: 
 
    print(nums[l][1], nums[r][1]) 
    l += 1
    r -= 1