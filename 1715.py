from heapq import heappop, heappush
import sys
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    heappush(q, int(input()))

total = 0
for _ in range(n-1):
    a, b = heappop(q), heappop(q)
    total += a+b
    heappush(q, a+b)
print(total)