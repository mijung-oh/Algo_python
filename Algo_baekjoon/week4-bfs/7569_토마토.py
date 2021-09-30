def bfs():
    # 익은 토마토를 한바퀴 다 돌면서 
    # 배열에 인접한 토마토 위치를 넣는다.
    # 베열 딥카피 성능 ?
    # 배열을 바로 빈 배열로 덮어씌우는거 괜찮은지
    global tomato, visited
    day = 0
    while tomato:
        cur = tomato[::]
        tomato = []
        for c in cur:
            # 해당 토마토와 인접한 토마토를 다 tomato 안에 넣는다.
            for d in [(0,0,1), (0,0,-1), (0,-1,0), (0,1,0), (1,0,0), (-1,0,0)]:
                nn = (c[0] + d[0]) % N
                nm = c[1] + d[1]
                nh = c[2] + d[2]
                
                # 만약 방문한 곳이었다면 pass
                if (nn, nm, nh) in visited:
                    continue

                if 0<= nn < N and 0 <= nm < M and 0 <= nh < H:
                    tomato.append((nn, nm, nh))
                    visited.append((nn, nm, nh))
                    print(nn, nm, nh)
                    day += 1
    return day
            
            
    


M, N, H = map(int, input().split())

# 가로: 0~M-1, 세로: 0~N-1, 높이: 0~H-1
BRD = []
h = 0
for i in range(N * H):
    sub = list(map(int, input().split()))

    if i >= N and i % N == 0:
        h += 1
    sub.append(h)
    BRD.append(sub)


tomato = []
visited = []
for n in range(0, N*H):
    for m in range(M):
        if BRD[n][m] == 1:
            # 익은 토마토의 위치를 저장한다.
            tomato.append((n%N, m, h))
            visited.append((n%N, m, h))


print(bfs())