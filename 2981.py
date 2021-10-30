#어렵다...

import sys, math
input = sys.stdin.readline

n = int(input())
gcd = 0
nums = []
for i in range(n):
    nums.append(int(input()))
    if i == 1:
        gcd = abs(nums[0] - nums[1])
    gcd = math.gcd(nums[i]-nums[i-1], gcd)
max_range = int(gcd**0.5)
result = [gcd]
for i in range(2, max_range+1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd//i)
result = list(set(result))
result.sort()
print(*result)