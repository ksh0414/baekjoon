x = int(input())
a, b = 1, 2
for _ in range(x-2):
    a, b = b, (a+b)%15746
print(b if x != 1 else 1)