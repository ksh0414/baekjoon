import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = set()
    for i in range(1, v+1):
        if i in visited:
            continue
        visited.add(i)
        group = [set([i]), set()]
        q = deque([(0, i)])
        while q:
            idx, now = q.popleft()
            n_idx = (idx+1)%2
            for n_n in graph[now]:
                if n_n not in visited:
                    group[n_idx].add(n_n)
                    q.append((n_idx, n_n))
                    visited.add(n_n)
                else:
                    if n_n in group[idx]:
                        return False
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    if bfs():
        print('YES')
    else:
        print('NO')
