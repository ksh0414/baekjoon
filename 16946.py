import sys
from collections import deque
input = sys.stdin.readline
D = ((1, 0), (0, 1), (-1, 0), (0, -1))

n, m = map(int, input().split())
board = []
walls = []
for i in range(n):
    board.append([int(x) for x in input().rstrip()])
    for j in range(m):
        if board[i][j] == 1: walls.append((i, j))

visited = [[-1] * m for _ in range(n)]
order = 0
group = []
for x, y in walls:
    total = 0
    union = []

    for dx, dy in D:
        nx, ny = x+dx, y+dy
        if not (0<=nx<n and 0<=ny<m):
            continue

        if board[nx][ny] == 0 and visited[nx][ny][0] == 0:
            q = deque([(nx, ny)])
            cnt = 1
            while q:
                i, j = q.popleft()
                for di, dj in D:
                    ni, nj = i+di, j+dj
                    if 0<=ni<n and 0<=nj<m and board[ni][nj] == 0 and visited[ni][nj] == 0:
                        visited[ni][nj] = order
                        q.append((ni, nj))
                        cnt += 1
            order += 1
            group.append(cnt)

        if visited[nx][ny] not in union:
            total += group[visited[nx][ny]]
            union.append(visited[nx][ny])

    board[x][y] = (total+1)%10

for z in board:
    print("".join([str(x) for x in z]))