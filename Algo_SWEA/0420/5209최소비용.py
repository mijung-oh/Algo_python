T = int(input())


def back(row_number, total, visited):
    global min_total
    if row_number == len(BRD):
        if min_total > total:
            min_total = total
        return min_total
    
    for i in range(len(BRD)):
        if total + BRD[row_number][i] < min_total and visited[i] == 0:
            visited[i] = 1
            back(row_number + 1, total + BRD[row_number][i], visited)
            visited[i] = 0

    return min_total


for tc in range(1, T+1):
    N = int(input())
    BRD = [list(map(int, input().split())) for _ in range(N)]
    min_total = 0xffff
    visited = [0] * len(BRD)
    print('#{} {}'.format(tc, back(0, 0, visited)))
