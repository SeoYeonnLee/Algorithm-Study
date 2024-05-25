c = int(input())

for _ in range(c):
    score = list(map(int, input().split()))
    score_mean = sum(score[1:]) / score[0]
    high_score = 0

    for s in score[1:]:
        if s > score_mean:
            high_score += 1
    
    print(f'{high_score / score[0] * 100:.3f}%')