def solution(dirs):
    x, y = 5, 5
    
    dir_set = set()
    
    for d in dirs:
        if d == 'U':
            nx, ny = x, y+1
        elif d == 'D':
            nx, ny = x, y-1
        elif d == 'R':
            nx, ny = x+1, y
        else:
            nx, ny = x-1, y
        
        if (not (0<=nx<=10)) or (not (0<=ny<=10)):
            continue
        
        dir_set.add((x, y, nx, ny))
        dir_set.add((nx, ny, x, y))
        
        x, y = nx, ny
        
    answer = len(dir_set) / 2
    
    return answer