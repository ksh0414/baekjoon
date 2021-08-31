import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
point = [int(input()) for _ in range(n)]
now = m = 0
visited = set()
flag = True
while now != k:
    if now not in visited:
        visited.add(now)
        m += 1
        now = point[now]
    else:
        flag = False
        break
print(m if flag else -1)