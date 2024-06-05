N = int(input())

def fac(n):
    res = 1
    if n > 0:
        res = n * fac(n-1)
    return res

print(fac(N))