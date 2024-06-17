import sys
from collections import deque

T = int(sys.stdin.readline())

def ac(fun, length, nums):
    num_arr = deque(nums)
    if length == 0:
        num_arr = deque()
    reverse = False
    
    for f in fun:
        if f == 'R':
            reverse = not reverse

        elif f == 'D':
            if not num_arr:
                return 'error'
            elif reverse == False:
                num_arr.popleft()
            else:
                num_arr.pop()

    if reverse == True:
        num_arr.reverse()

    return '[' + ','.join(num_arr) + ']'

for _ in range(T):
    fun = sys.stdin.readline()
    length = int(sys.stdin.readline())
    nums = sys.stdin.readline().rstrip()[1:-1].split(',')

    print(ac(fun, length, nums))