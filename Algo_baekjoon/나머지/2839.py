# N = int(input())


# five_max = 5000//5
# three_max = 5000//3
# min_count = three_max
# for i in range(three_max,-1,-1):
#     total = 3*i
#     if total == N and i < min_count:
#         min_count = i
#     else:
#         for j in range(0,five_max+1):
#             total = 5*j + 3*i
#             if total == N and i + j < min_count:
#                 min_count = i+j
#             elif total > N:
#                 break

    
# print(min_count if min_count != three_max else -1)


# DP bottom up 
# N = int(input())
# dp = [0xffffffff]* (N+5)

# dp[0] = dp[1] = dp[2] = dp[4] = 0
# dp[3] = 1
# dp[5] = 1
# for i in range(3, N):
#     if dp[i]:
#         dp[i + 3] = min(dp[i+3], dp[i]+1)    
#         dp[i + 5] = min(dp[i+5], dp[i]+1) 

# if dp[N] == 0 or dp[N] == 0xffffffff:
#     print('-1')
# else:
#     print(dp[N])

# DP top down
N = int(input())
dp = [0] * (N+6)
dp[0] = dp[1] = dp[2] = dp[4] = -1
dp[3] = dp[5] = 1
def topDown(N):
    if dp[N] == 0:
        if N-3>=0 and dp[N-3] == 0:
            a = topDown(N-3)
        else:
            a = dp[N-3]

        if N-5>=0 and dp[N-5] == 0:
            b = topDown(N-5)
        else:
            b = dp[N-5]
        if N == 4:
            print(b)
        dp[N-3] = a if a != -1 else 0xffffffff
        dp[N-5] = b if b != -1 else 0xffffffff

        dp[N] = min(dp[N-3]+1, dp[N-5]+1)
        return dp[N]
    elif dp[N] == -1:
        return -1
    else:
        return dp[N]

topDown(N)
if dp[N] == -1 or dp[N] == 0xffffffff + 1:
    print('-1')
else:
    print(dp[N])