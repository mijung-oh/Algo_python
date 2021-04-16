T = int(input())

# 완전탐색
def bruteforce(r,c,total):
    global minV
    if total > minV:
        return False
    if r == c and r == N-1:
        total += BRD[r][c]
        if total < minV:
            minV = total
            return minV
        else:
            return False
    if c+1 < N:
        bruteforce(r,c+1, total + BRD[r][c])
            
    if r+1 < N:
        bruteforce(r+1, c, total + BRD[r][c])
    return minV
            
    
# 메모이제이션
def memo(r,c):
    print(r,c)
    if r==c and r==0:
        return BRD[0][0]
    
    if r-1 >= 0 and c-1 >= 0:
        dist[r][c] = min(memo(r-1, c), memo(r,c-1)) + BRD[r][c]
    elif r-1 >= 0 and c-1 < 0:
        dist[r][c] = memo(r-1, c) + BRD[r][c]
    else:
        dist[r][c] = memo(r,c-1) + BRD[r][c]
    return dist[r][c]
    

for tc in range(1, T+1):
    minV = 999999
    N = int(input())
    BRD = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0 for _ in range(N)] for _ in range(N)]
    memo(N-1, N-1)
    print('#{} {}'.format(tc, dist[N-1][N-1]))
    # print('#{} {}'.format(tc, bruteforce(0,0,0)))

