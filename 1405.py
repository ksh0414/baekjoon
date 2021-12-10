D = ((0 ,1), (0, -1), (1, 0), (-1, 0))

def dfs(c, x, y, route, index, v):
    if c == data[0]:
        global ans
        ans += v
        return
            
    for i in index:
        dx, dy = D[i]
        n_x, n_y = x+dx, y+dy
        if board[n_x][n_y] == 0:
            board[n_x][n_y] = 1
            route.append(i+1)
            v *= data[i+1]
            dfs(c+1, n_x, n_y, route, index, v)
            v /= data[i+1]
            route.pop()
            board[n_x][n_y] = 0

data = list(map(int, input().split()))
for i in range(1, 5):
    data[i] /= 100
board = [[0] * 29 for _ in range(29)]
board[14][14] = 1

index = []
for i in range(4):
    if data[i+1] != 0:
        index.append(i)
ans = 0
dfs(0, 14, 14, [], index, 1)
print(ans)