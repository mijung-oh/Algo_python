def solution(stones, k):
    answer = 0

    # 연속된 0의 개수가 k-1 이하여야 가능하다.
    def count():
        maxV = -1
        l = 0
        r = len(stones)-1
        # 문자열 길이가 1일 경우
        if l == r:
            if stones[l]:
                return 1
            else:
                return -1

        l_cnt = r_cnt = 0
        while l <= r:
            if l == r:
                if stones[l] == 0:
                    return max(maxV, max(l_cnt, r_cnt) + 1)
                return maxV

            if stones[l] == 0:
                l_cnt += 1
            else:
                l_cnt = 0

            if stones[r] == 0:
                r_cnt += 1
            else:
                r_cnt = 0
            
            maxV = max(maxV, max(l_cnt, r_cnt))

            if maxV >= k:
                return maxV
            
            # r = l+1일 경우
            if r == l+1:
                if stones[l] == 0 and stones[r] == 0:
                    return max(maxV, l_cnt + r_cnt)
            l += 1
            r -= 1
        return maxV



    while 1:
        cnt = count()
        if cnt == -1:
            break
        if cnt >= k:
            break

        answer += 1
        # 1씩 차감한다.
        for i in range(len(stones)):
            if stones[i]:
                stones[i] -= 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))