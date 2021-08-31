import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
point = [int(input()) for _ in range(n)]
order = [-1] * n
for i in range(n):
    order[point[i]] = i+1
    if point[i] == k:
        break
print(order[k])