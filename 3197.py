import sys
from collections import deque
input = sys.stdin.readline
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
JUDGE = [-3, -2, 0]
BLOCK = [-2, -3, 1]

def bfs(a, b, v, n_s, j):
    if board[a][b] != v:
        return False
    q = deque([(a, b)])
    board[a][b] = BLOCK[j]
    while q:
        #print(q)
        x, y = q.popleft()
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if 0<=nx<r and 0<=ny<c:
                if board[nx][ny] == v:
                    board[nx][ny] = BLOCK[j]
                    q.append((nx, ny))
                elif board[nx][ny] == -1:
                    board[nx][ny] = v+1
                    n_s[j].append((nx,ny))
                elif board[nx][ny] == JUDGE[j]:
                    return True
    return False
                
def play(v):
    global spot
    next_spot = [[], [], []]
    for i in range(3):
        while spot[i]:
            if bfs(*spot[i].pop(), v, next_spot, i):
                return True
    spot = next_spot
    BLOCK[2] += 1
    return False
        
r, c = map(int, input().split())
board = [[0]*c for _ in range(r)]
spot = [[], [], []]
count = 0
for i in range(r):
    line = input().rstrip()
    for j in range(c):
        if line[j] == 'L':
            spot[count].append((i, j))
            count += 1
        elif line[j] == 'X':
            board[i][j] = -1
        else:
            spot[2].append((i, j))
time = 0
while not play(time):
    time += 1
print(time)