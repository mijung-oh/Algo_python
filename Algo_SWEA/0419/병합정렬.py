T = int(input())


def mergeSort(a):
    global result_cnt
    if len(a) == 1: return a
    
    mid = len(a)//2
    left = mergeSort(a[:mid])
    right = mergeSort(a[mid:])

    if left[-1] > right[-1]: result_cnt += 1

    k = 0
    result = []
    i=j=0
    # Merge
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result


for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    result_mid = len(lst)//2
    result_cnt = 0
    result = mergeSort(lst)
    print('#{} {} {}'.format(tc, result[result_mid], result_cnt))