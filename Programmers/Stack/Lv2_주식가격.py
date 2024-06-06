def solution(prices):
    stack = []
    n = len(prices)
    seconds = [0] * n
    
    for i, p in enumerate(prices):
        while stack and p < prices[stack[-1]]:
            j = stack.pop()
            seconds[j] = i - j
        
        stack.append(i)
    
    while stack:
        j = stack.pop()
        seconds[j] = n - 1 - j
        
    return seconds