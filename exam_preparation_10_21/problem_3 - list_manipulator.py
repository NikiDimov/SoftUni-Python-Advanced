def list_manipulator(seq, act, pos, *args):
    if act == 'add' and pos == 'beginning':
        return list(args) + seq
    if act == 'add' and pos == 'end':
        return seq + list(args)
    if act == 'remove' and pos == 'beginning':
        if args:
            return seq[args[0]:]
        else:
            return seq[1:]
    if act == 'remove' and pos == 'end':
        if args:
            return seq[:len(seq) - args[0]]
        else:
            return seq[:-1]