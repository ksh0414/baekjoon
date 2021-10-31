import sys
from heapq import heappop, heappush
input = sys.stdin.readline
START, END = 0, 1

n = int(input())
lectures = []
for _ in range(n):
    lectures.append(tuple(map(int, input().split())))
lectures.sort()

q = [0]
for x_s, x_e in lectures:
    if q[0] <= x_s:
        heappop(q)
    heappush(q, x_e)
print(len(q))