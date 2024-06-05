def solution(string):
    answer = 0
    n = len(string)
    
    for i in range(n):
        stack = []
        for j in range(n):
            b = string[(i+j) % n]
            
            if (b == '(') or (b == '{') or (b == '['):
                stack.append(b)
            else:
                if not stack:
                    break

                if b == ')' and stack[-1] == '(':
                    stack.pop()
                elif b == '}' and stack[-1] == '{':
                    stack.pop()
                elif b == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
                
    return answer