from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for order in orders:
            # 1. 각 메뉴별로 조합을 구한다(단, 메뉴는 2개 이상으로)
            for _li in combinations(order, k):
                res = ''.join(sorted(_li))
                candidates.append(res)
        # 2. 카운터 정렬
        sorted_candidates = Counter(candidates).most_common()

        # 카운트가 2 이상이면서 가장 첫번째 키운터 원소와 같은 것만 answer에 넣는다.
        for menu, cnt in sorted_candidates:
            if cnt>1 and cnt == sorted_candidates[0][1]:
                answer.append(menu)
    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
