a = [5,6,1,8,9,4,2,6,8,4]

def selectionSort(lst):
    for i in range(len(lst)):
        target = i
        for j in range(i+1, len(lst)):
            if lst[target] > lst[j]:
                target = j
        lst[i], lst[target] = lst[target], lst[i]

    return lst


#  재귀 선택 정렬 알고리즘
def recurSelectionSort(target, lst):
    if target == len(lst)-1:
        return
    min_idx = target
    for i in range(target+1, len(lst)):
        if lst[min_idx] > lst[i]:
            min_idx = i
    lst[min_idx], lst[target] = lst[target], lst[min_idx]
    print(target, recurSelectionSort(target+1, lst))
    return lst
print(recurSelectionSort(0, a))
    