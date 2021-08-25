import sys
input = sys.stdin.readline

ropes = []
for _ in range(int(input())):
    ropes.append(int(input()))

k = 0
max_weight = 0
for rope in sorted(ropes, reverse = True):
    k += 1
    tmp = rope*k
    if tmp > max_weight:
        max_weight = tmp
print(max_weight)