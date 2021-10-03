while True:
    a, b = map(int, input().split())
    if a != b:
        ans = 'factor'
        if a > b:
            a, b = b, a
            ans = 'multiple'
        if b % a == 0:
            print(ans)
        else:
            print('neither')
    else:
        break