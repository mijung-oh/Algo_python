T = int(input())

#테스트케이스
for t in range(1, T+1):
    N, M = map(int, input().split())
    # 이중 리스트 만들기
    fly = []
    for i in range(N):
        fly.append(list(map(int, input().split())))
    max_dead = -1
    # 파리채가 갈 수 있는 경로 (i, j)
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                
                total += sum(fly[i+k][j:j+M])

            if max_dead < total:
                max_dead = total

    print(f'#{t} {max_dead}')
                
