
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    res = 0
    for i in range(0, b):
        res = add(res, a)
    return res


print(mul(2, 3))
