from itertools import permutations

def solution(A, B):
    answer = 0
    # 오름차순으로 A와 B를 정렬한다.
    A.sort()
    B.sort()

    # A를 돌면서 B의 원소가 더 클 경우 answer +1 해준다.
    b_idx = 0
    for a in A:
        # 이미 A 원소보다 큰 B 원소는 없으므로
        if b_idx >= len(B): break

        # A 원소보다 큰 B 원소를 찾으면 바로 break
        while b_idx < len(B):
            if a < B[b_idx]:
                answer += 1
                b_idx += 1
                break
            b_idx += 1

    print(answer)
    return answer
solution([2,2,2,2], [1,1,1,1])