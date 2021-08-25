import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    grades = [0] * (n+1)
    for _ in range(n):
        a, b = map(int, input().split())
        grades[a] = b
    min = n+1
    ans = 0
    for grade in grades[1:]:
        if grade < min:
            min = grade
            ans += 1
    print(ans)