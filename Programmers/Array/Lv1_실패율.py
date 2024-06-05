def solution(N, stages):
    fake_rate = {}
    
    for stage in range(1, N+1):
        reach = sum([1 if s >= stage else 0 for s in stages])
        
        if reach == 0:
            fake_rate[stage] = 0
            continue
            
        fake_rate[stage] = stages.count(stage) / reach
        
    answer = sorted(fake_rate, key = lambda x: fake_rate[x], reverse=True)
    
    return answer