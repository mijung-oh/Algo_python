T = int(input())

# 순열
# 처음과 끝은 항상 1이기 때문에
# 1로 시작하는 순열을 구한 뒤 뒤에 1을 붙여주어서
# 해당 값을 더해준다.
def perm(n, k):
    global arr, min_sum
    
    if k == n:
        total = 0
        arr2 = arr + [1]
        for i in range(len(arr2)-1):
            total += BRD[arr2[i]-1][arr2[i+1]-1]
        if total < min_sum:
            min_sum = total

    # 순열구하는 코드
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

for tc in range(1, T+1):
    N = int(input())
    BRD = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(1, N+1)]
    n = len(arr)
    min_sum = 0xfffffff

    perm(n, 1)
    print('#{} {}'.format(tc, min_sum))
