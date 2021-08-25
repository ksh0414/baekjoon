n = int(input())
data = list(map(int, input().split()))
data.sort()
time = 0
accumulation = 0
for x in data:
    time += accumulation + x
    accumulation += x
print(time)