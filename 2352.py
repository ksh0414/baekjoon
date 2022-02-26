import sys
from bisect import bisect_left as bisect
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
inc_list = []

for x in nums:
    index = bisect(inc_list, x)
    if index >= len(inc_list):
        inc_list.append(x)
    inc_list[index] = x

print(len(inc_list))