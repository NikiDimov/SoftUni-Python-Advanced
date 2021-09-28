def math_operations(*args, **kwargs):
    args = list(args)[::-1]
    while args:
        for key, value in kwargs.items():
            if not args:
                break
            if key == 'a':
                kwargs['a'] += args.pop()
            elif key == 's':
                kwargs['s'] -= args.pop()
            elif key == 'd':
                divider = args.pop()
                if divider == 0:
                    continue
                else:
                    kwargs['d'] /= divider
            elif key == 'm':
                kwargs['m'] *= args.pop()
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))

