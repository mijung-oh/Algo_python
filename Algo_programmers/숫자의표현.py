def solution(n):
    answer = 0
    for i in range(1, n):
        sub_sum = i
        for j in range(i+1, n):
            sub_sum += j
            if sub_sum == n:
                print(i, j)
                answer += 1
            elif sub_sum > n:
                break
    print(answer+1)
    return answer+1

solution(10)