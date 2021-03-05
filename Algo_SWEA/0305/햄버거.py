T = int(input())

# 조합으로 부분집합 구한 다음에
# 구해진 원소들의 칼로리의 합이 칼로리보다 낮으면서 최대점수보다 큰 경우
# 최대점수 초기화해주기
def powerset(N, max_sum, L):
    for i in range(1<<N):
        # score은 서브 점수, sum은 서브 칼로리 총합
        sub_score = 0
        sub_sum = 0
        for j in range(N):
            if i & 1<<j:
                sub_score += hamburger[j][0]
                sub_sum += hamburger[j][1]
                if sub_sum >= L:
                    break
        if sub_sum < L and sub_score > max_sum:
            max_sum = sub_score
    return max_sum

for tc in range(1, T+1):
    N, L = map(int, input().split())
    hamburger = []
    for n in range(N):
        hamburger.append((list(map(int, input().split()))))

    max_sum = -1
    print('#{} {}'.format(tc,powerset(N, max_sum, L)))

