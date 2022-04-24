import sys
from xml.dom import minicompat
input = sys.stdin.readline

N = int(input())
result = 0
matrix = []
for n in range(N):
    r, c = map(int, input().split())
    matrix.append((r,c))

dp = [[2 ** 31] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
# ABC => 012
for i in range(1, N): # 행렬 곱하기 개수 i = 2
    for j in range(N-i): # 행렬 곱셈 시작 j = 0 
        for k in range(j, j+i): # k = 0, 1
            # 00 12 = A * BC
            # 01 22 = AB * C
            left = (matrix[j][0], matrix[k][1])
            right = (matrix[k+1][0], matrix[i+j][1])
            sub_sum = left[0] * left[1] * right[1]
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][i+j] + sub_sum)
print(dp[0][N-1])