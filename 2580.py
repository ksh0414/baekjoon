def dfs(cnt):
    if cnt == l:
        for line in board:
            print(' '.join(map(str, line)))
        exit(0)
    
    x, y = pos[cnt]
    for i in range(1, 10):
        if not row_arr[x][i] and not col_arr[y][i] and not box_arr[3*(x//3)+(y//3)][i]:
            row_arr[x][i] = col_arr[y][i] = box_arr[3*(x//3)+(y//3)][i] = True
            board[x][y] = i
            dfs(cnt+1)
            row_arr[x][i] = col_arr[y][i] = box_arr[3*(x//3)+(y//3)][i] = False
            board[x][y] = 0

N = 9
board = [list(map(int, input().split())) for _ in range(9)]
row_arr = [[False]*10 for _ in range(10)]
col_arr = [[False]*10 for _ in range(10)]
box_arr = [[False]*10 for _ in range(10)]
pos = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0: pos.append((i, j))
        else:
            row_arr[i][board[i][j]] = True
            col_arr[j][board[i][j]] = True
            box_arr[3*(i//3)+(j//3)][board[i][j]] = True

l = len(pos)