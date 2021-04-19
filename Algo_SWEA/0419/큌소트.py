# def Partition(lst, left, right):
#     pivot = lst[left]
#     i = left
#     j = right
#     while i<j:
#         while lst[j] > pivot: j -= 1
#         while i<j and lst[i] <= pivot: i += 1

#         lst[i], lst[j] = lst[j], lst[i]
    
#     lst[j], lst[left] = lst[left], lst[j]
#     return j


# def QuickSort(lst, left, right):
#     if left >= right:
#         return

#     pivot_idx = Partition(lst, left, right)
#     QuickSort(lst, left, pivot_idx-1)
#     QuickSort(lst, pivot_idx+1, right)
            

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     QuickSort(lst, 0, len(lst)-1)
#     print(lst[N//2])

# 1. 퀵소트 함수적용 
def quick_sort(numbers):
    # 길이가 1보다 작으면 숫자 반환 (빈 값도 고려)
    if len(numbers) <= 1:
        return numbers
    # 기준값은 첫번째 인덱스
    pibut = numbers[0]
    left = []
    right = []

    # 첫번째 인덱스를 기준으로 두번째부터 끝까지 pibut보다 작으면 왼쪽리스트로 같거나크면 오른쪽리스트로 append
    for i in range(1, len(numbers)):
        if numbers[i] < pibut:
            left.append(numbers[i])
        else:
            right.append(numbers[i])
            
    # 왼쪽 오른쪽으로 1회 정렬된 리스트를 첫번째 길이가 1보다 작거나같냐는 if문에 걸릴 때 까지 재귀
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    print(sorted_left,sorted_right)
    
    # 리스트로 출력하기 때문에 리스트 안에 대괄호 제거를 위해 *추가해서 결과 반환 
    return [*sorted_left, pibut, *sorted_right]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    # 1. 퀵소트 함수적용 
    sorted_lst = quick_sort(lst)
    print(sorted_lst)
    # 2. 결과값 출력(중간값)
    print(f'#{tc} {sorted_lst[len(sorted_lst)//2]}')

    