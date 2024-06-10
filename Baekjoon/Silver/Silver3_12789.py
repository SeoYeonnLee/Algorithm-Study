import sys
from collections import deque

N = int(sys.stdin.readline())
line = map(int, sys.stdin.readline().split())

def snack(N, line):
    line = deque(line)
    wait = []

    cnt = 1

    while line:
        if cnt == line[0]:
            line.popleft()
            cnt += 1
        elif wait and cnt == wait[-1]:
            wait.pop()
            cnt += 1
        else:
            tmp = line.popleft()
            wait.append(tmp)

    while wait:
        w = wait[-1]
        if w == cnt:
            wait.pop()
            cnt += 1
        else:
            return 'Sad'

    return 'Nice'

print(snack(N, line))