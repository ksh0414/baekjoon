import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def bfs(start, k):
  global graph
  queue = deque([start])
  visited = [False] * (n+1)
  count = 0
  while queue:
    now = queue.popleft()
    visited[now] = True
    for n_n, w in graph[now]:
      if w < k or visited[n_n]:
        continue
      count += 1
      queue.append(n_n)
  print(count)

n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

for _ in range(q):
  k, v = map(int, input().split())
  bfs(v, k)