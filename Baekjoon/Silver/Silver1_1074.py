import sys

N, r, c = map(int, sys.stdin.readline().split())
cnt = 0

def Z_search(N, r, c):
    global cnt

    if N == 1:
        cnt += (2*r + c)
        return

    if (2 ** N) // 2 > r:
        if (2 ** N) // 2 > c:
            Z_search(N-1, r, c)
        else:
            cnt += int((2 ** N)**2 * (1/4))
            Z_search(N-1, r, c - 2**(N-1))
    else:
        if (2 ** N) // 2 > c:
            cnt += int((2 ** N)**2 * (2/4))
            Z_search(N-1, r - 2**(N-1), c)
        else:
            cnt += int((2 ** N)**2 * (3/4))
            Z_search(N-1, r - 2**(N-1), c - 2**(N-1))

Z_search(N, r, c)
print(cnt)