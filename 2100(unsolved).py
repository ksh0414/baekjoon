import sys
A = ord('A')

towers = [[] for _ in range(26)]
for _ in range(int(input())):
    a, b, c = input().rstrip().split()
    towers[ord(a)-A].append((int(b), int(c)))

for t in towers:
    t.sort()