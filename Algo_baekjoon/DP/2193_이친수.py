N = int(input())

# dp[i] = (a,b) => i개수로 이루어져 있으면서 0으로 끝나는 숫자 개수 a
# 1로 끝나는 숫자 개수 b

# dp[1]= 1,0 - 1
# dp[2] = 0,1 - 10
# dp[3] = 100, 101 => 1, 1
# dp[4] = 1000, 1001, 1010 => 1, 2
# dp = [[0,0] for _ in range(N+1)]
# if N ==1:
#     print(1)
#     exit()

# dp[2] = [1,0]
# for i in range(3, N+1):
#     # 전에서 0으로 끝나는 숫자에 0과 1을 붙이면 되므로
#     dp[i][0] = dp[i-1][1] + dp[i-1][0]

#     # 전에서 1로 끝나는 숫자에 0을 붙이면 되므로
#     dp[i][1] = dp[i-1][0]
# print(sum(dp[N]))

# 두번째 풀이
a, b = 1, 0
for i in range(3, N+1):
    a, b = a+b, a
print(a+b)
