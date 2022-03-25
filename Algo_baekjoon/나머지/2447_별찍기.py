import sys
input = sys.stdin.readline
N = int(input())
Map = [[0 for _ in range(N)] for _ in range(N)]

def f(n):
    
    global N
    if n == 3:
        Map[0][:3] = Map[2][:3] = ['*'] * 3
        Map[1][0] = Map[1][2] = '*'
        return

    # n이 3이상일 경우 일단 3일때의 한 박스를 채우기
    f(n//3)
    
    K = n // 3
    # Map 채우기
    for i in range(3):
        for j in range(3):
            # 공백
            if i == 1 and j == 1:
                continue
            else:
                for k in range(K):
                    # 행씩 집어넣는다.
                    Map[K*i+k][K*j:K*(j+1)] = Map[k][:K]
    

f(N)
for i in range(N):
    for j in range(N):
        if Map[i][j] == 0:
            print(" ", end="")
            continue
        print(Map[i][j], end="")
    print()
