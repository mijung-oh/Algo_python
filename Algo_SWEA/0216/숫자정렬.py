T = int(input())

def selectionSort(lst):
    st = 0

    for i in range(len(lst)-1):
        # 최솟값있는 idx 찾기
        min_element = lst[i]
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < min_element:
                min_element = lst[j]
                min_idx = j
        # 찾으면 change
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst




for t in range(1, T+1):
    N = int(input())

    number = list(map(int, input().split()))
    result = selectionSort(number)
    print(f'#{t}', end=' ')
    for r in result:
        print(r, end=' ')
    print()