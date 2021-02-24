T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(input().split())

    first = []
    second = []
    # N이 홀수
    if N%2:
        for i in range(N//2+1):
            first.append(lst[i])
        for j in range(N//2+1, N):
            second.append(lst[j])
    else:
        for i in range(N//2):
            first.append(lst[i])
        for j in range(N//2, N):
            second.append(lst[j])

    result = []
    idx = 0
    while idx < len(first):
        result.append(first[idx])
        if idx<len(second):
            result.append(second[idx])
        idx += 1

    print('#{}'.format(tc), end=' ')
    print(*result)