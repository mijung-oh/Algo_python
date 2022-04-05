N = int(input())
arr = list(map(int, input().split()))

# 자기보다 큰 원소가 없는 경우
# 1로 표시
# 자기보다 큰 원소가 있는 경우
# +1을 각각 했을 때 가장 큰 값을 저장
# dp[i]: i 를 포함한 가장 긴 수열의 길이
dp = [0] * N
for idx, v in enumerate(arr):
    # 이전에 자기보다 큰 원소가 있는지 확인
    length = 0
    for i in range(idx):
        if v < arr[i]:
            length = max(length, dp[i])
    
    if length:
        dp[idx] = length + 1
    else:
        dp[idx] = 1
print(max(dp))
