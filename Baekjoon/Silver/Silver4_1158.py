import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

delete = []
queue = deque(range(1, N+1))

while len(queue) > 0:
    for _ in range(K-1):
        p = queue.popleft()
        queue.append(p)
    
    d = queue.popleft()
    delete.append(d)
    
delete = list(map(str, delete))
print('<'+', '.join(delete)+'>')