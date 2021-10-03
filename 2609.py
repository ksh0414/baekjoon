A, B = map(int, input().split())
if A < B:   A, B = B, A
a, b = A, B

while a % b != 0:
    a, b = b, a%b
print(b)
print(A*B//b)