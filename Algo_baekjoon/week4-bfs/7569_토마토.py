def bfs():
    # 익은 토마토를 한바퀴 다 돌면서 
    # 배열에 인접한 토마토 위치를 넣는다.
    # 베열 딥카피 성능 ?
    # 배열을 바로 빈 배열로 덮어씌우는거 괜찮은지
    global tomato, total
    day = 0
    while tomato:
        cur = tomato[::]
        tomato = []
        for c in cur:
            # 해당 토마토와 인접한 토마토를 다 tomato 안에 넣는다.
            # 위, 아래
            for d in [(N,0), (-N, 0)]:
                nn = c[0] + d[0]
                nm = c[1] + d[1]

                if 0<= nn < N*H and 0 <= nm < M and BRD[nn][nm] == 0:
                    tomato.append((nn, nm))
                    BRD[nn][nm] = 1
                    total += 1
            
            # 앞, 뒤
            for d in [(1,0), (-1, 0)]:
                nn = c[0] + d[0]
                nm = c[1] + d[1]

                if 0<= c[0] % N + d[0] < N and 0 <= nm < M and BRD[nn][nm] == 0:
                    tomato.append((nn, nm))
                    BRD[nn][nm] = 1
                    total += 1

            # 좌, 우
            for d in [(0,1), (0,-1)]:
                nn = c[0] + d[0]
                nm = c[1] + d[1]

                if 0<= nn < N*H and 0 <= nm < M and BRD[nn][nm] == 0:
                    tomato.append((nn, nm))
                    BRD[nn][nm] = 1
                    total += 1
        if tomato:         
            day += 1
        
    return day
            
            
    


M, N, H = map(int, input().split())

# 가로: 0~M-1, 세로: 0~N-1, 높이: 0~H-1
BRD = []
for i in range(N * H):
    sub = list(map(int, input().split()))
    BRD.append(sub)


tomato = []
total = 0
not_tomato = 0
for n in range(0, N*H):
    for m in range(M):
        if BRD[n][m] == 1:
            # 익은 토마토의 위치를 저장한다.
            tomato.append((n, m))
            total += 1
        elif BRD[n][m] == -1:
            total += 1
            not_tomato += 1

# 애초에 토마토가 다 익은 상태라면
if total == N*M*H:
    print("0")
else:
    result = bfs()
    if total != N*M*H or not_tomato == total:
        print("-1")
    else:
        print(result)