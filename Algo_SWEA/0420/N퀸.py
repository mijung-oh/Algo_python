T = int(input())

def back(row_number):
    global count, N
    if row_number == len(BRD):
        count += 1
        return True

    for i in range(len(BRD)):
        # print(visited[i], visited[row_number+i])
        # 열체크
        if col_visit[i]:
            continue
        # 오른쪽 대각선
        if visited[row_number+i]:
            continue
        # print('hi')
        # 왼쪽대각선
        k = row_number-i + (N-1)
        if cross_visit[k]:
            continue


        # 열, 대각선 다 안겹치면
        # visited 체크하고 다음 행으로
        col_visit[i] = True
        visited[row_number+i] = True
        cross_visit[row_number-i+N-1] = True
        back(row_number+1)

        col_visit[i] = False
        visited[row_number+i] = False
        cross_visit[row_number-i+N-1] = False
        
    return True
           


for tc in range(1, T+1):
    N = int(input())
    BRD = [[0 for _ in range(N)] for _ in range(N)]
    visited = [False] * ((N-1)*2+1)
    col_visit = [False] * N
    cross_visit = [False] * (N*2-1)
    count = 0
    back(0)


    print('#{} {}'.format(tc, count))