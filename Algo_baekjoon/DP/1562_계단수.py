N = int(input())
# [비트마스킹][현재까지 길이][마지막 숫자]
dp = [[[-1] * 11 for i in range(101)] for _ in range(1<<11)]

cnt = 0
mod = 1000000000
def dfs(bit, cur_len, cur_num):
    global cnt, N, mod
    if cur_num < 0 or cur_num > 9: return 0

    # 현재까지 길이가 N과 같다면 
    if cur_len == N:
        # 비트마스킹이 다 체크 되었다면
        if bit == (1<<10) - 1:
            return 1
        else:
            return 0

    # dp에 값이 있다면
    if dp[bit][cur_len][cur_num] != -1:
        return dp[bit][cur_len][cur_num]
    dp[bit][cur_len][cur_num] = 0
    
    # 현재 숫자가 0이라면
    if cur_num == 0:
        dp[bit][cur_len][cur_num] += dfs(bit | (1 << (cur_num+1)), cur_len+1, cur_num+1)
        dp[bit][cur_len][cur_num] %= mod
    elif cur_num == 9:
        dp[bit][cur_len][cur_num] += dfs(bit | (1 << (cur_num-1)), cur_len+1, cur_num-1)
        dp[bit][cur_len][cur_num] %= mod
    else:
        dp[bit][cur_len][cur_num] += dfs(bit | (1 << (cur_num+1)), cur_len+1, cur_num+1)
        dp[bit][cur_len][cur_num] %= mod
        dp[bit][cur_len][cur_num] += dfs(bit | (1 << (cur_num-1)), cur_len+1, cur_num-1)
        dp[bit][cur_len][cur_num] %= mod

    return dp[bit][cur_len][cur_num]

for i in range(1, 10):
    # 1 dfs(1000000000, 1, 9)
    # dfs() 1000000000 | 1<<8 => 1000000000 |
    # 123456789 => 1111111111
    cnt += dfs(1<<i, 1, i)
    cnt %= mod

print(dp)

print(cnt)
