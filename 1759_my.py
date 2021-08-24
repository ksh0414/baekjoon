from itertools import combinations

l, c = map(int, input().split())
vowels = []
consonants = []
for x in input().split():
    if x in ('a', 'e', 'i', 'o', 'u'):
        vowels.append(x)
    else:
        consonants.append(x)

ans = []
for vc in range(max(1, l-len(consonants)), (l-2)+1):
    for x in combinations(vowels, vc):
        for y in combinations(consonants, l - vc):
            tmp = list(x + y)
            tmp.sort()
            ans.append(''.join(tmp))

ans.sort()
for x in ans:
    print(x)