def solution(id_list, report, k):
    report_dict = {}
    message_cnt = {}
    
    for r in report:
        p1, p2 = r.split()
        if p2 not in report_dict:
            report_dict[p2] = set()
        report_dict[p2].add(p1)
        
    for id in id_list:
        message_cnt[id] = 0
    
    for r, people in report_dict.items():
        if len(report_dict[r]) >= k:
            for p in people:
                message_cnt[p] += 1

    return list(message_cnt.values())