import sys
input  = sys.stdin.readline
D = ((1, 0), (0, 1), (-1, 0), (0, -1))

def dfs(t, x, y, arr):
    if t == 5:
        global ans
        ans.add(tuple(arr))
        return

    for dx, dy in D:
        nx, ny = x+dx, y+dy
        if 0<=nx<5 and 0<=ny<5:
            arr.append(board[nx][ny])
            dfs(t+1, nx, ny, arr)
            arr.pop()
    

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

ans = set()
for i in range(5):
    for j in range(5):
        dfs(0, i, j, [board[i][j]])

print(len(ans))