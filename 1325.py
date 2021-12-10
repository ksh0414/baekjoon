import sys
input = sys.stdin.readline

def bfs(s):
    visted = [0]*(N+1)
    visted[s] = 1
    q = [s]
    
    c = 1
    while q:
        now = q.pop()
        for n_n in graph[now]:
            if visted[n_n] == 0:
                visted[n_n] = 1
                q.append(n_n)
                c += 1
    
    return (c, s)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_value = 0
ans = []
for s in range(1, N+1):
    value, idx = bfs(s)
    if max_value < value:
        ans = []
        ans.append(idx)
        max_value = value
    elif max_value == value:
        ans.append(idx)

print(*sorted(ans))