T = int(input())

min_sum = 1e10
BRD = []


def powerset(N, k, arr, visited, sel, sub):
    global min_sum
    if sub > min_sum:
        return
    if k == N:
        sub_sum = 0
        for i in range(N):
            sub_sum += BRD[i][sel[i]]
        if sub_sum < min_sum:
            min_sum = sub_sum
        return
    for i in range(N):
        if visited[i]:continue
        visited[i] = 1
        sel[k] = arr[i]
        print(sub)
        powerset(N, k+1, arr, visited, sel, sub+BRD[k][arr[i]])
        visited[i]=0

for tc in range(1, T+1):
    N = int(input())
    # 순열 모음
    total = []
    arr = []
    sel = [0]*N
    visited = [0]*N

    for n in range(N):
        BRD.append(list(map(int, input().split())))
    # 열의 인덱스 순열로 뽑기 위해
    for i in range(N):
        arr.append(i)
    powerset(N, 0, arr, visited, sel, 0)

    print('#{} {}'.format(tc, min_sum))
    min_sum = 1e10
    BRD = []