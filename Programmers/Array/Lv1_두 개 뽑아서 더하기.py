def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            res = numbers[i] + numbers[j]
            if res not in answer:
                answer.append(res)
    answer.sort()
    return answer