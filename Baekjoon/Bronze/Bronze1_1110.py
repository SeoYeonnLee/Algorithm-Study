import sys

N = int(sys.stdin.readline())
new = 10 * (N%10) + (N//10 + N%10)%10
cnt = 1

while True:
    if new == N:
        break
    new = 10 * (new%10) + (new//10 + new%10)%10
    cnt += 1

print(cnt)