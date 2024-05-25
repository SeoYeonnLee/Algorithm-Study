import sys

X = int(sys.stdin.readline())

cnt = 0
line = 1

while cnt + line < X:
    cnt += line
    line += 1

divisor = X - cnt

if (line + 1) % 2 == 0:
    print(f'{line + 1 - divisor}/{divisor}')
else:
    print(f'{divisor}/{line + 1 - divisor}')