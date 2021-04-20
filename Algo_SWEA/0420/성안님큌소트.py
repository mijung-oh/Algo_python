def quicksort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        if p == N//2: # 답을 미리 찾아버리면 끝
            return
        # p 기준 왼쪽 정렬
        quicksort(arr, l, p-1)
        # p 기준 오른쪽 정렬
        quicksort(arr, p+1, r)


def partition(arr, l, r):
    pivot = (l + r) // 2

    while l < r:
        while arr[l] < arr[pivot] and l < r:
            l+=1
        while arr[r] >= arr[pivot] and l < r:
            r-=1
        if l<r:
            if l == pivot:
                pivot = r
            #swap
            arr[l], arr[r] = arr[r], arr[l]
    arr[pivot], arr[r] = arr[r], arr[pivot]
    return r


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    # 정렬한 값 넣기
    quicksort(lst, 0, N-1)
    print(lst)
    print("#{} {}".format(tc, lst[N//2]))