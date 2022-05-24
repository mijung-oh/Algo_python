def solution(n, times):
    answer = 0
    # 1부터 최악의 경우 발생하는 시간을 저장한다.
    l, r = 1, max(times) * n

    while l < r:
        # 1과 최악의 경우 걸리는 시간의 중간값
        mid = (l + r) // 2

        # 이 중간값으로 사람을 계산할 경우 몇명을 심사할 수 있는지 확인한다.
        people = 0
        for t in times:
            people += mid // t

            # 만약 people이 n보다 크거나 같을 경우 더 셀 필요가 없으므로
            # 빠져나온다.
            if people >= n: break
        
        if people >= n:
            r = mid 
        else:
            l = mid + 1
    answer = l
    return answer

'''
def solution(n, times):
    answer = 0
    # 1부터 최악의 경우 발생하는 시간을 저장한다.
    l, r = 1, max(times) * n

    while l <= r:
        # 1과 최악의 경우 걸리는 시간의 중간값
        mid = (l + r) // 2

        # 이 중간값으로 사람을 계산할 경우 몇명을 심사할 수 있는지 확인한다.
        people = 0
        for t in times:
            people += mid // t

            # 만약 people이 n보다 크거나 같을 경우 더 셀 필요가 없으므로
            # 빠져나온다.
            if people >= n: break
        
        if people >= n:
            answer = mid
            r = mid-1
        else:
            l = mid + 1
    return answer
'''