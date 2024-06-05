def solution(answers):
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0] * 3
    
    for i, ans in enumerate(answers):
        for j, pat in enumerate(pattern):
            if ans == pat[i % len(pat)]:
                scores[j] += 1
    
    answer = []
    max_score = max(scores)
    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i+1)
    
    return answer