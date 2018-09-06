memory = {}

def count(target, rest, level):
    if (rest, level) in memory:
        return memory[(rest,level)]
    if rest == 0:
        return 1
    if level == 0 or rest < 0:
        return 0
    ret = ret = count(target, rest, level - 1)
    if rest - level - level >= 0:
        ret += count(target, rest - level, level)
    else:
        ret += count(target, rest - level, level - 1)
    memory[(rest, level)] = ret
    return ret

n = 100
result = count(n, n, n - 1)
print(result)
