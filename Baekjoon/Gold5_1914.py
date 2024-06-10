import sys

N = int(sys.stdin.readline())
process = []

def hanoi(n, fr, tmp, to):
    global cnt, process

    if n == 1:
        print(fr, to)
        return
    
    hanoi(n-1, fr, to, tmp)
    print(fr, to)
    hanoi(n-1, tmp, fr, to)

print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)