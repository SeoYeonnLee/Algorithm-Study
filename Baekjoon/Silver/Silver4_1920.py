import sys

N = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
compare_num = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, num, start, end):
    if start >  end:
        return 0
    mid = (start + end) // 2

    if arr[mid] == num:
        return 1
    elif arr[mid] > num:
        return binary_search(arr, num, start, mid-1)
    else:
        return binary_search(arr, num, mid+1, end)
    
for n in compare_num:
    print(binary_search(num_list, n, 0, len(num_list)-1))