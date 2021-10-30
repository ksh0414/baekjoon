for _ in range(int(input())):
    try:
        case = input()
        stk = []
        for x in case:
            if x == '(':
                stk.append(x)
            else:
                stk.pop()
        print('NO' if stk else 'YES')
    except:
        print('NO')