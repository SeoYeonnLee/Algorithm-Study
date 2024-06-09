from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for g in goal:
        if cards1 and g == cards1[0]:
            cards1.popleft()
        elif cards2 and g == cards2[0]:
            cards2.popleft()
        else:
            return 'No'

    return 'Yes'