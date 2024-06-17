from itertools import combinations

def solution(orders, course):
    
    menu_cnt = {}
    course_menu = {}
    answer = []
    
    for c in course:
        course_menu[c] = set()
        for order in orders:
            for combi in combinations(order, c):
                course_menu[c].add(''.join(sorted(combi)))
                menu_cnt[''.join(sorted(combi))] = menu_cnt.get(''.join(sorted(combi)), 0) + 1

    for c in course:
        max_cnt = 0
        max_menu = []

        for m in course_menu[c]:
            if menu_cnt[m] > 1:
                if menu_cnt[m] > max_cnt:
                    max_menu.clear()
                    max_menu.append(m)
                    max_cnt = menu_cnt[m]
                elif menu_cnt[m] == max_cnt:
                    max_menu.append(m)

        answer.extend(max_menu)
    
    return sorted(answer)