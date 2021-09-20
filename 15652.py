def back_tracking(idx, cnt):
    if cnt == m:
        print(*result)
        return
    for i in range(idx, n+1):
        result.append(i)
        back_tracking(i, cnt+1)
        result.pop()

n, m = map(int, input().split())
result = []
back_tracking(1, 0)