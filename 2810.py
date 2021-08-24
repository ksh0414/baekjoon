n = int(input())
count = 0
lcount = 0
for x in list(input()):
    if x == 'S':
        count += 1
    else:
        lcount += 1
count += lcount // 2 + 1
print(min(n, count))