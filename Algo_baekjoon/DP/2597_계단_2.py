N = int(input())
stairs = [0]
for n in range(N):
    stairs.append(int(input()))

if N == 1:
    print(stairs[1])
    exit()
elif N == 2:
    print(stairs[1] + stairs[2])
    exit()
else:
    # dp[i] = i번째까지 오는데 최댓값
    dp = [0] * (N+1)

    # 현재 노드의 최댓값은 
    # 자신의 계단 값 + 바로 전 단계 계단 + 3번째 아래 계단
    # 자신의 계단 + 2번째 아래 계단 의 최댓값이다.
    # 마지막 노드 계단도 함께 해결
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[2] + stairs[3], stairs[1] + stairs[3])

    for i in range(4, N+1):
        dp[i] = max(dp[i-2] + stairs[i], stairs[i] + stairs[i-1] + dp[i-3])
    print(dp[N])