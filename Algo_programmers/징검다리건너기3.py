def solution(stones, k):
    answer = 0

    while 1:
        check = True
        for idx in range(len(stones)-k+1):
            # k길이만큼을 가져와서
            if stones[idx:idx+k].count(0) >= k:
                check = False
                break
        if not check: break

        answer += 1
        # 1씩 차감한다.
        for i in range(len(stones)):
            if stones[i]:
                stones[i] -= 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))