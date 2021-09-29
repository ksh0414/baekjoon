import sys
from bisect import bisect_right
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(tuple(map(int, input().split())))
data.sort()

lis = []
for _, x in data:
    idx = bisect_right(lis, x)
    if idx >= len(lis):
        lis.append(x)
    else:
        lis[idx] = x
print(N-len(lis))