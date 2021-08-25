import sys
input = sys.stdin.readline

timetable = []
for _ in range(int(input())):
    timetable.append(tuple(map(int, input().split())))
now = 0
ans = 0
for s, e in sorted(timetable):
    if now <= s:
        now = e
        ans += 1
    elif e < now:
        now = e
print(now)
print(ans)