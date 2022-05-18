# N = int(input())
# answer = 1 # 아예 배치하지 않는 경우
# # 1마리씩만 배치하는 경우
# answer += N * 2
# # N마리 다 배치하는 경우
# answer += 2
# print(answer)

# # 배치 수
# for i in range(2, N):
#     # 시작하는 라인의 행 
#     for j in range(N-i+1):
#         # 2마리 => 0,1,2행까지
#         # 3마리 => 0,1행까지
#         # i마리 => N-i+1
#         print(i, "마리", j, "행", ((N-(j+1))*2-1)*2)
#         answer += ((N-(j+1))*2-1)*2
# print(answer)

N = int(input())
MOD = 9901
# dp[a][b] => a행에 b가 0이면 사자가 없음. 1이면 사자가 왼쪽. 2이면 사자가 오른쪽
dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0][0] = dp[0][1] = dp[0][2] = 1

for i in range(1, N):
    # i번째 행에 사자가 없으면 i-1행에 사자가 어디에 있든 상관 없음
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
    # i번째 행에 왼쪽에 사자가 있다면 i-1행은 사자가 있거나 오른쪽에 있어야함
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD

print(sum(dp[N-1]))