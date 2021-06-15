N = int(input())

pho = [0]
for n in range(N):
    pho.append(int(input()))
dp = [0] * (N+4)
# 1,2,3번이 있을 때
# dp[1] = pho[1]'
if N == 1:
    dp[1] = pho[1]
elif N>1:
    dp[1] = pho[1]
    dp[2] = pho[1] + pho[2]
    for i in range(3, N+1):
        # 1번 + 3번
        # 2번+3번
        # 3번을 선택하지 않는 경우
        dp[i] = max(dp[i-1], dp[i-2] + pho[i], dp[i-3] + pho[i-1] + pho[i])

print(dp[N])
                                                                                                                                                                                                                                                                                                                                                                                                           