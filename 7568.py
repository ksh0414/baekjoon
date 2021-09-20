n = int(input())
people = []
for i in range(n):
    tmp = list(map(int, input().split()))
    tmp.append(i)
    people.append(tmp)

people.sort()
result = [1] * n
for i in range(n):
    w, h, idx = people[i]
    for ww, hh, _ in people[i+1:]:
        if w < ww and h < hh:
            result[idx] += 1

print(*result)