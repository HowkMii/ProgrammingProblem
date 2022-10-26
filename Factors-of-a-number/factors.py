from math import sqrt, ceil, floor, gcd, log2, factorial

def factors(n):

    res = []

    for i in range(1, int(sqrt(n)) + 1):
        if (n % i) == 0:

            if n // i == i:
                res.append(i)
            else:
                res.append((i, n//i))

    return res


ans = factors(8)

print(ans)