import sys
from collections import deque
input = sys.stdin.readline
D = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs():
    q = deque([(0, 0)])
    board[0][0] = 1
    while q:
        i, j = q.popleft()
        now = board[i][j]
        for di, dj in D:
            ni, nj = i+di, j+dj
            if 0<=ni<r and 0<=nj<c and board[ni][nj] == '1':
                board[ni][nj] = now+1
                q.append((ni, nj))
    return board[r-1][c-1]

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input().strip()))
print(bfs())