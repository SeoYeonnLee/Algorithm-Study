import sys

N = int(sys.stdin.readline())

def group_word(string):
    str_set = {string[0]}
    for s in range(1, len(string)):
        if string[s] == string[s-1]:
            continue
        else:
            if string[s] in str_set:
                return 0
            else:
                str_set.add(string[s])
    return 1

cnt = 0
for _ in range(N):
    word = sys.stdin.readline()
    cnt += group_word(word)
print(cnt)