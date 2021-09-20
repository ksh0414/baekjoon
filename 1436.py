n = int(input())
cnt = 0
flag = '666'
num = 666
while cnt < n:
    ans = str(num)
    if flag in ans:
        cnt += 1
    num += 1
print(ans)