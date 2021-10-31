#그리디 사고방식 연습하자
import sys
input = sys.stdin.readline
A, B = 0, 1

def convert(i, j):
    for r in range(i, i+3):
        for c in range(j, j+3):
            matrixes[A][r][c] = 1 - matrixes[A][r][c]

N, M = map(int, input().split())
matrixes = [[], []]
for i in range(2):
    for _ in range(N):
        matrixes[i].append(list(map(int, list(input().rstrip()))))
ans = 0
for i in range(N-2):
    for j in range(M-2):
        if matrixes[A][i][j] != matrixes[B][i][j]:
            convert(i, j)
            ans += 1

print(ans if matrixes[A] == matrixes[B] else -1)