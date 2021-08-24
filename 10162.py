T = int(input())
ans = []
for unit in (300, 60, 10):
    tmp = 0
    while T - unit >= 0:
        T -= unit
        tmp += 1
    ans.append(f'{tmp}')
print(' '.join(ans) if T == 0 else - 1) #join함수는 list의 element가 모두 str이어야한다