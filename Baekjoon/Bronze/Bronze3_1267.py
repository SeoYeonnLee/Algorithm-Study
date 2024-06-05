import sys

N = int(sys.stdin.readline())
call_list = list(map(int, sys.stdin.readline().split()))

Y_list = [(call//30 + 1)*10 for call in call_list]
M_list = [(call//60 + 1)*15 for call in call_list]

Y_sum = sum(Y_list)
M_sum = sum(M_list)

if Y_sum < M_sum:
    print('Y', Y_sum)

elif Y_sum > M_sum:
    print('M', M_sum)

else:
    print('Y', 'M', Y_sum)