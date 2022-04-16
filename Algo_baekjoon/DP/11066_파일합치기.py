import sys
input = sys.stdin.readline

T = int(input())




for t in range(T):
    N = int(input())
    files = list(map(int, input().split()))
    dp = [[99999999 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        dp[i][i] = 0

    # for i in range(N):
    #     for j in range(N):
    #         if i != j:
    #             d = sum(files[i:j+1])
    #             minimum = 99999999
    #             for k in range(j):
    #                 print(i, j, k, dp[i][k], dp[k+1][j])
    #                 minimum = min(minimum, dp[i][k] + dp[k+1][j])
    #                 print(minimum)
    #             dp[i][j] = d + minimum

    for i in range(1, N): # 부분 파일의 길이 1 2 3
        for j in range(N-1): # 시작점 0 1 2 3
            # 0 2 = 00 12 / 01 22
            d = sum(files[j:i+j+1])
            minimum = 99999999
            for k in range(j, i+j):
                print(i, j, k, i+j)
                minimum = min(minimum, dp[j][k] + dp[k+1][i+j])
            print(i, j, d, minimum)
            dp[j][j+i] = d + minimum
    for i in range(len(dp)):
        print(*dp[i])
    print(dp[i][N-1])