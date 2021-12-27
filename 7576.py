import sys
from collections import deque
input = sys.stdin.readline
D = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(arr, count):
    ans = 0
    total = len(arr)
    q = deque(arr)
    while q:
        ans += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0<=nx<r and 0<=ny<c and board[nx][ny] == 0:
                    q.append((nx, ny))
                    board[nx][ny] = 1
                    total += 1        
                    
    return ans-1 if total == count else -1

c, r = map(int, input().split())
board = []
tomatos = []
count = r*c
for i in range(r):
    board.append(list(map(int, input().split())))
    for j in range(c):
        if board[i][j] == 1:
            tomatos.append((i, j))
        elif board[i][j] == -1:
            count -= 1
print(bfs(tomatos, count))