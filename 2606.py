import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = set([1])
    q = deque([1])

    while q:
        now = q.popleft()
        for n_n in graph[now]:
            if n_n not in visited:
                visited.add(n_n)
                q.append(n_n)
    return len(visited)-1
        

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(bfs())