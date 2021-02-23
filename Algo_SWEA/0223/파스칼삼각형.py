T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = [0]*N
    for i in range(N):
        if i == 0:
            result[i] = [1]
        elif i == 1:
            result[i] = [1,1]
        else:
            t = []
            for j in range(i+1):
                if j == 0 or j == i:
                    t.append(1)
                else:
                    t.append(result[i-1][j-1]+result[i-1][j])
            result[i] = t

    print('#{}'.format(tc))
    for i in range(N):
        print(*result[i])