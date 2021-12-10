from collections import deque

n, m = map(int, input().split())

q = deque([[n, 0, [n]]])
visited = [0]*100001
visited[n] = 1
if n <= m:
    while True:
        now, t, route = q.popleft()
        if now == m:
            break
        
        for dx in [1, -1, now]:
            n_n = now+dx
            if not 0<=n_n<=100000:
                continue
            if visited[n_n] != 1:
                visited[n_n] = 1
                q.append((n_n, t+1, [*route, n_n]))
    print(t)
    print(*route)
else:
    print(n-m)
    print(*list(range(n, m-1, -1)))