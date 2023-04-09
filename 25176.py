N = int(input())


def chungjung(a):
    if (a > 0):
        result = (a * chungjung(a - 1))
        return result
    else:
        return 1


print(chungjung(N))