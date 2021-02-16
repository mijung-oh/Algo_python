T = int(input())
def binarySearch(x, arr):
    count = 0
    left = 0
    right = len(arr)-1
    mid = (left+right)//2
    while 1:
        count += 1
        if left > right:
            break
        if x == arr[mid]:
            return count
        if arr[left] <= x < arr[mid]:
            right = mid
            mid = (left + right) // 2
        elif arr[mid] < x <= arr[right]:
            left = mid
            mid = (left + right) // 2
    return 0

for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    page = list(range(1, P+1))
    Ca = binarySearch(Pa, page)
    Cb = binarySearch(Pb, page)
    if Ca < Cb:
        win = 'A'
    elif Ca > Cb:
        win = 'B'
    else:
        win = 0
    print(f'#{t} {win}')