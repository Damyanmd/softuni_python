def func_executor(*args):
    result = []
    for function_name, data in args:
        res = function_name(*data)
        result.append(res)
    return result