import sys
from collections import deque

test_num = int(sys.stdin.readline())

def printer_queue(N, i, importance):
    idx = deque(range(N))
    importance = deque(importance)
    criterion = importance[i]
    greater = sum([val > criterion for val in importance])
    max_importance = max(importance)
    cnt = 0

    while cnt < greater:
        if importance[0] == max_importance:
            importance.popleft()
            idx.popleft()
            cnt += 1
            max_importance = max(importance)
        else:
            move = importance.popleft()
            importance.append(move)
            m = idx.popleft()
            idx.append(m)

    while idx[0] != i:
        if importance[0] == criterion:
            idx.popleft()
            importance.popleft()
            cnt += 1
        else:
            idx.popleft()
            importance.popleft()
            
    return cnt + 1

for _ in range(test_num):
    N, i = map(int, sys.stdin.readline().split())
    importance = map(int, sys.stdin.readline().split())
    print(printer_queue(N, i, importance))