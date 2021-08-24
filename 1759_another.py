from itertools import combinations

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()

for case in combinations(alpha, l):
    vc = cc = 0

    for x in case:
        if x in ('a', 'e', 'i', 'o', 'u'):
            vc += 1
        else:
            cc += 1
        if vc >= 1 and cc >= 2:
            break
    else:
        continue
    print(''.join(case))