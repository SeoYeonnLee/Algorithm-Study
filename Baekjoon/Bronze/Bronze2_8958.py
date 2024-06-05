n = int(input())

for _ in range(n):
    res = input()

    cor = 0
    score = 0

    for s in res:
        if s == 'O':
            cor += 1
            score += cor
        else:
            cor = 0

    print(score)