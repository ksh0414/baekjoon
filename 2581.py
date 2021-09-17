m, n = int(input()), int(input())
prime = [i for i in range(n+1)]
prime[1] = 0
for i in range(2, int(n**0.5)+1):
    for j in range(2, (n//i)+1):
        prime[i*j] = 0
sum_prime = 0
min_prime = 0
for i in range(m, n+1):
    if prime[i] != 0:
        min_prime = i
        sum_prime += sum(prime[i:n+1])
        break
    sum_prime += prime[i]
if sum_prime:
    print(sum_prime, min_prime, sep = '\n')
else:
    print(-1)