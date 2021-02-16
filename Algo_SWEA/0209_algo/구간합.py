T = int(input())

for t in range(1, T+1):
    N, M = input().split()
    N, M = int(N), int(M)
    lst = list(map(int, input().split()))

    # 초기화
    maxS = minS = 0
    for i in range(M):
        print(i)
        maxS += lst[i]
    minS = maxS


    for l in range(0, N-M+1):
        temp = 0
        for k in range(l, l+M):
            temp+= lst[k]

        if maxS < temp:
            maxS = temp
        if minS > temp:
            minS = temp

    print(maxS - minS)