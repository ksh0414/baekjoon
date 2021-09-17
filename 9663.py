import sys
sys.setrecursionlimit(10**9)

def back_tracking(i, j, cnt):
    global ans
    if cnt == n:
        ans += 1
        return

    for x in range(i, n):
        for y in range(n):
            if check(x, y):
                board[x][y] = 1
                back_tracking(x, y, cnt+1)
                board[x][y] = 0

def check(i, j):
    base = i-0
    for x in range(n):
        if board[i][x] == 1 or board[x][j] == 1:
            return False
        if 0<=j-base+x<n and board[x][j-base+x] == 1:
            return False
        if 0<=j+base-x<n and board[x][j+base-x] == 1:
            return False
    return True

n = int(input())
board = [[0]*n for _ in range(n)]
ans = 0
back_tracking(0, 0, 0)
print(ans)