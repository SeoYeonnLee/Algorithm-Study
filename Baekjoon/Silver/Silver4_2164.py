import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque(range(1, N+1))

while len(queue) > 1:
    queue.popleft()
    move = queue.popleft()
    queue.append(move)

print(queue[0])