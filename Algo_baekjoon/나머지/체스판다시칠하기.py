N, M = map(int, input().split())
BRD = []
for n in range(N):
    BRD.append(list(input()))

count = 0xffffffff
for i in range(N-8+1):
    for j in range(M-8+1):
        # W로 시작하는 경우
        countW = 0
        # B로 시작하는 경우
        countB = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                # x+y가 홀수일 경우 시작점과 달라야한다.
                if (x+y) % 2:
                    if BRD[x][y] == 'W':
                        # W일 경우 시작점이 W일 때 문제가 됨
                        countW += 1
                    elif BRD[x][y] == 'B':
                        countB += 1

                else:
                    if BRD[x][y] == 'B':
                        # 시작점이 B일 때 문제가 됨
                        countW += 1
                    elif BRD[x][y] == 'W':
                        # 시작점이 W일 때 문제가 됨
                        countB += 1

        count = min(count, countW, countB)
print(count)
        