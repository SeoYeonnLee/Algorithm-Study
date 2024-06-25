def solution(enroll, referral, seller, amount):
    answer = {}
    people_dict = {}

    for i in range(len(enroll)):
        people_dict[enroll[i]] = referral[i]
        answer[enroll[i]] = 0
    
    for i, sell in enumerate(seller):
        earn = 100 * amount[i]
        
        while earn >= 10:
            give = int(earn * 0.1)

            if people_dict[sell] == '-':
                earn = earn - give
                break

            answer[sell] += earn - give

            earn = give
            sell = people_dict[sell]
        
        answer[sell] += earn
    
    return list(answer.values())