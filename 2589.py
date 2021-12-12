import sys
from collections import deque
input = sys.stdin.readline
D = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(i, j):
    visited = set([(i, j)])
    q = deque([(0, i, j)])
    value = 0
    
    while q:
        cost, x, y = q.popleft()
        value = max(cost, value)
        
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if (nx, ny) in visited:
                continue
            if 0<=nx<r and 0<=ny<c and board[nx][ny] == 'L':
                q.append((cost+1, nx, ny))
                visited.add((nx, ny))
    
    return value

r, c = map(int, input().split())
board = []
lands = []
for i in range(r):
    board.append(input().rstrip())
    for j in range(c):
        if board[i][j] == 'L':
            lands.append((i, j))

ans = 0
for i, j in lands:
    ans = max(ans, bfs(i, j))

print(ans)