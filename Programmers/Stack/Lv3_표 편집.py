def solution(n, k, cmd):
    delete = []
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]
    k += 1
    
    for c in cmd:
        if c == 'C':
            delete.append(k)
            down[up[k]] =down[k]
            up[down[k]] = up[k]
            k = up[k] if down[k] > n else down[k]
        
        elif c == 'Z':
            re = delete.pop()
            down[up[re]] = re
            up[down[re]] = re
        
        else:
            move, num = c.split()
            if move == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
    
    answer = ['O'] * n
    while delete:
        d = delete.pop()
        answer[d-1] = 'X'

    return ''.join(answer)