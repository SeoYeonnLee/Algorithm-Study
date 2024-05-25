N = int(input())

def palindrome(n):
    global cnt
    cnt += 1

    if (len(n) == 0) or (len(n) == 1):
        return 1
    
    if n[0] == n[-1]:
        return palindrome(n[1:-1])
    else:
        return 0

for _ in range(N):
    cnt = 0
    string = input()
    print(palindrome(string), cnt)