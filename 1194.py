import sys
from collections import deque
input = sys.stdin.readline
D = [[1, 0], [0, 1], [-1, 0], [0, -1]]
a = ord('a')
convert = {chr(a+i): 1 << i for i in range(6)}

def bfs(a, b):
    q = deque([(0, a, b, 0)])
    visited = [[[0]*(1<<6) for _ in range(C)] for _ in range(R)]
    visited[a][b][0] = 1
    while q:
        cost, x, y, nkeys = q.popleft()
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if 0<=nx<R and 0<=ny<C and visited[nx][ny][nkeys] == 0:
                visited[nx][ny][nkeys] = 1
                if board[nx][ny] == '#':
                    pass
                elif board[nx][ny] == '.':
                    q.append((cost+1, nx, ny, nkeys))
                elif board[nx][ny] == '1':
                    return cost+1
                else:
                    if convert[board[nx][ny].lower()] & nkeys:
                        q.append((cost+1, nx, ny, nkeys))
                    elif 'a'<=board[nx][ny]<='z':
                        nkeys += convert[board[nx][ny]]
                        q.append((cost+1, nx, ny, nkeys))
                        nkeys -= convert[board[nx][ny]]
    
    return -1

R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(list(input().rstrip()))
    for j in range(C):
        if board[i][j] == '0':
            start = (i, j)
            board[i][j] = '.'

print(bfs(*start))