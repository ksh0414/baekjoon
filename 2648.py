from itertools import combinations

MOVE = {'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)}
X, Y = 0, 1

x, y = map(int, input().split())
point = set()
vertex = set()
for _ in range(int(input())):
    vertex.add((x, y))
    a, b = input().split()
    b = int(b)
    d = MOVE[a]
    dx, dy = d[X], d[Y]
    for _ in range(b):
        x, y = x+dx, y+dy
        if (x, y) in point:
            vertex.add((x, y))
        else:
            point.add((x, y))
area = 101*101
for n_p1, n_p2 in combinations(vertex, 2):
    if n_p1[X] == n_p2[X] or n_p1[Y] == n_p2[Y]:
        continue
    if (n_p1[X], n_p2[Y]) in vertex and (n_p2[X], n_p1[Y]) in vertex:
        n_area = abs((n_p1[X]-n_p2[X])*(n_p1[Y]-n_p2[Y]))
        if n_area < area:
            area = n_area
            p1, p2 = n_p1, n_p2

if area != 101*101:
    x1, x2 = sorted([p1[X], p2[X]])
    y1, y2 = sorted([p1[Y], p2[Y]])
    print(x1, y1)
    print(x2, y2)
else:
    print(0)