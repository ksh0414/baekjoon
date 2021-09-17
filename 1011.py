import math

for _ in range(int(input())):
    start, end = map(int, input().split())
    end -= start
    n = math.ceil((-1+(1+8*(end//2))**0.5)/2)
    end -= n*(n+1)//2
    n += math.ceil((-1+(1+8*end)**0.5)/2)
    print(n)