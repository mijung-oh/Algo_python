T = int(input())

for t in range(1, T+1):
    N = int(input())
    color = [[0 for x in range(10)] for y in range(10)]

    for n in range(N):
        # 색칠할 영역과 색깔을 받음
        x1,y1,x2,y2,c = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                color[i][j] += c

    count = 0
    for i in range(10):
        for j in range(10):
            if color[i][j] == 3:
                count += 1
    print(f'#{t} {count}')