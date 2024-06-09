from collections import deque

def solution(progresses, speeds):
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    
    while progresses:
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        answer.append(cnt)
        
    return answer