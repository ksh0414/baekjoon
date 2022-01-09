import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()
idx=sum=0
while (idx+1)<n: #음수 처리
    if nums[idx] < 0:
        if nums[idx+1] <= 0:
            sum += nums[idx]*nums[idx+1]
            idx += 2
        else:
            sum += nums[idx]
            idx += 1
    else:
        break
try:
    while nums[idx] <= 1: #1처리
        sum += nums[idx]
        idx += 1
    if ((n-1) - idx)%2 == 0: #양수 처리
        sum += nums[idx]
        idx += 1
    for i in range(n-2, idx-1, -2):
        sum += nums[i]*nums[i+1]
except:
    pass
finally:
    print(sum)