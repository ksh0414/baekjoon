import sys
input = sys.stdin.readline

n = int(input())
nums = []
total = 0
for _ in range(n):
    x = int(input())
    if x != 1:
        nums.append(x)
    else:
        n -= 1
        total += x
nums.sort(reverse=True)
stop = 0
for i in range(1, n, 2):
    stop = i+1
    if nums[i] <= 0:
        if nums[i-1] > 0:
            total += nums[i-1]
            stop = i
        else:
            stop = i-1
        break
    total += nums[i-1]*nums[i]
for i in range(n-2, stop-1, -2):
    total += nums[i]*nums[i+1]
if n>0 and (stop+n)%2:
    total += nums[stop]
print(total)