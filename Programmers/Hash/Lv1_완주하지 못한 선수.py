def solution(participant, completion):
    dic = {}
    
    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    
    for c in completion:
        if dic[c] == 1:
            del dic[c]
        else:
            dic[c] -= 1
    
    return list(dic.keys())[0]