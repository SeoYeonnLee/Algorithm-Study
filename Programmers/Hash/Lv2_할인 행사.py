def solution(want, number, discount):
    dis_dic = {}
    want_dic = {}
    cnt = 0
    N = len(discount)
    
    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    for d in discount[:10]:
        if d in dis_dic:
            dis_dic[d] += 1
        else:
            dis_dic[d] = 1
    
    if dis_dic == want_dic:
        cnt += 1

    for idx in range(10, N):

        if discount[idx] in dis_dic:
            dis_dic[discount[idx]] += 1
        else:
            dis_dic[discount[idx]] = 1
        
        dis_dic[discount[idx-10]] -= 1
        
        if dis_dic[discount[idx-10]] == 0:
            del dis_dic[discount[idx-10]]

        if dis_dic == want_dic:
            cnt += 1
            
    return cnt