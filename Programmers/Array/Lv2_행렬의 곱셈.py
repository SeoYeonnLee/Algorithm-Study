def solution(arr1, arr2):
    l, m, n = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0] * n for _ in range(l)]
    
    for i in range(l):
        for j in range(n):
            for k in range(m):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            
    return answer