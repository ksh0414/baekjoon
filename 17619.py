import sys
import bisect
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n, q = map(int, input().split())
logs = [(-1, -1, 0)]
parents = [i for i in range(n+1)]
pos = []
for i in range(1, n+1):
    x1, x2, y = map(int, input().split())
    logs.append((x1, x2, i))
logs.sort()
x, y, _ = logs[1]
for i in range(2, n+1):
    nx, ny, _ = logs[i]
    if nx <= y:
        union(logs[i-1][2], logs[i][2])
        y = max(ny, y)
    else:
        x, y = nx, ny

for _ in range(q):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(1)
    else:
        print(0)
        