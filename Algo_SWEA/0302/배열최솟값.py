T = int(input())
total = []
def powerset(N, k, arr, visited, sel):
    if k == N:
        # 딥카피를 안할 경우 total은 sel에 대한 주소공간을 가지고 있기때문에 같은 값만 나온다.
        total.append(sel[::])
        return
    for i in range(N):
        if visited[i]:continue
        visited[i] = 1
        sel[k] = arr[i]
        powerset(N, k+1, arr, visited, sel)
        visited[i]=0

for tc in range(1, T+1):
    N = int(input())
    BRD = []

    # 순열 모음
    total = []

    arr = []
    sel = [0]*(N+1)
    visited = [0]*(N+1)

    for n in range(N):
        BRD.append(list(map(int, input().split())))
    # 열의 인덱스 순열로 뽑기 위해
    for i in range(N):
        arr.append(i)
    powerset(N, 0, arr, visited, sel)

    min_sum = 100000
    for t in total:
        sub_sum = 0
        for i in range(N):
            sub_sum += BRD[i][t[i]]
        if sub_sum < min_sum:
            min_sum = sub_sum
    print('#{} {}'.format(tc, min_sum))
    total = []