def even_odd(*args):
    if args[-1] == 'even':
        args = args[:-1]
        result = list(filter(lambda x: x % 2 == 0, args))
        return result
    else:
        args = args[:-1]
        result = list(filter(lambda x: x % 2 != 0, args))
        return result