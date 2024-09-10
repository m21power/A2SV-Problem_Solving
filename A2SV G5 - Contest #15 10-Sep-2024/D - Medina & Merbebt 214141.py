# Problem: D - Medina & Merbebt - https://codeforces.com/gym/522079/problem/D

t = int(input())
for _ in range(t):
    n = int(input()) 
    nums = list(map(int, input().split()))  
    q = int(input()) 

    arr = [0] * 32
    prefix = [arr]  # Initialize prefix array with zeros

    # Calculate prefix sums of bits
    for num in nums:
        arr = prefix[-1].copy()
        for i in range(32):
            # If the i-th bit is set in num, increment the corresponding count in arr
            if num & (1 << i) != 0:
                arr[i] += 1
        prefix.append(arr)

    # Function to find the bitwise AND of all numbers within a range
    def rangeAnd(l, r):
        ans = 0
        for i in range(32):
            bit_count = prefix[r][i] - prefix[l - 1][i] if l > 0 else prefix[r][i]
            if bit_count == (r - l + 1):
                ans |= (1 << i)
        return ans

    # Binary search to find the rightmost index satisfying the condition
    def bin_search(l, k):
        left = l
        right = n
        while left <= right:
            mid = (right + left) // 2
            if rangeAnd(l, mid) >= k:
                left = mid + 1
            else:
                right = mid - 1

        if right < l:
            return -1
        return right

    ans = []
    # Process queries
    for _ in range(q):
        l, k = map(int, input().split())
        ans.append(bin_search(l, k))

 
    print(*ans)