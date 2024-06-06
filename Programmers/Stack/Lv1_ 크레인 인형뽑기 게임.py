def solution(board, moves):
    answer = 0
    stack = []
    
    for m in moves:
        for line in board:
            if line[m-1] != 0:
                doll = line[m-1]
                if (not stack) or (stack[-1] != doll):
                    stack.append(doll)
                elif stack[-1] == doll:
                    stack.pop()
                    answer += 2
                line[m-1] = 0
                break
        
    return answer