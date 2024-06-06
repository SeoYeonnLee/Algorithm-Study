def solution(string):
    stack = []
    
    for s in string:
        if not stack:
            stack.append(s)
        elif stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    
    if stack:
        return 0
    else:
        return 1