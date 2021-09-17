x = int(input())
mod = 2
while x > 1:
    if x % mod == 0:
        print(mod)
        x //= mod
    else:
        mod += 1