import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    x, y = a, b
    if x < y:
        x, y = y, x
    while y != 0:
        x, y = y, x%y
    print(a*b//x)