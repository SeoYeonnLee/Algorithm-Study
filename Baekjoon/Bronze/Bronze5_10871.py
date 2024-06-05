N, X = map(int, input().split())
num = list(map(int, input().split()))

res = [str(n) for n in num if n < X]
print(' '.join(res))