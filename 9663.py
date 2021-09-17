#배열을 통한 조건검사가 훨씬 빠르다
def back_tracking(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            back_tracking(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

n = int(input())
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
ans = 0
back_tracking(0)
print(ans)