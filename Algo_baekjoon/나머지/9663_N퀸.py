N = int(input())

# 방향은 왼쪽 위, 위, 오른쪽 위
d = [(-1,-1), (-1,0), (-1,1)]

BRD = [[0 for _ in range(N)] for _ in range(N)]

def dfs(r):
    if r == N-1:
        return True
    # 해당 행의 열을 탐색함
    for i in range(N):
        # 왼쪽 위, 위에, 오른쪽 위 
        for j in range(3):
            if BRD[i][]


    
    
    
dfs(0,0)

