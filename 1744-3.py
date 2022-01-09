import sys
input = sys.stdin.readline

n = int(input())
positive = []
negative = []
sum = 0
for _ in range(n):
    x = int(input())
    if x < 1:
        negative.append(x)
    elif x > 1:
        positive.append(x)
    else:
        sum += 1

positive.sort(reverse=True)
negative.sort()

if len(positive)%2:
    for i in range(1, len(positive)-1, 2):
        sum += positive[i]*positive[i-1]
    sum += positive[len(positive)-1]
else:
    for i in range(1, len(positive), 2):
        sum += positive[i]*positive[i-1]
        
if len(negative)%2:
    for i in range(1, len(negative)-1, 2):
        sum += negative[i]*negative[i-1]
    sum += negative[len(negative)-1]
else:
    for i in range(1, len(negative), 2):
        sum += negative[i]*negative[i-1]
print(sum)