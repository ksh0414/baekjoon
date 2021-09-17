import sys
input = sys.stdin.readline

max_num = 123456
prime = [i for i in range(2*max_num+1)]
prime[1] = 0
for i in range(2, int(((2*max_num)**0.5)+1)):
    for j in range(2, ((2*max_num)//i)+1):
        prime[i*j] = 0

while True:
    num = int(input())
    if num == 0:
        break
    print(num-prime[num+1:2*num+1].count(0))