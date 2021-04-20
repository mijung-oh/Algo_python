import sys
sys.stdin = open('input.txt', 'r')
T = int(input())


def back(row_number, total):
    global max_total
    if row_number == len(BRD):
        if max_total < total:
            max_total = total
        return max_total
    
    for i in range(len(BRD)):
        if BRD[row_number][i]:
            c = (total * BRD[row_number][i]) / 100

            if c > max_total and visited[i] == 0:
                visited[i] = 1
                back(row_number + 1, c)
                visited[i] = 0

    return max_total


for tc in range(1, T+1):
    N = int(input())
    BRD = [list(map(int, input().split())) for _ in range(N)]
    max_total = -1
    visited = [0] * len(BRD)
    result = back(0, 1) * 100
    print('#{} {:0.6f}'.format(tc, round(result, 6)))
