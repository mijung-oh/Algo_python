# import sys
# sys.stdin = open('이진탐색.txt', 'r')
T = int(input())

def binarySearch(lst, x):
    left = 0
    right = len(lst)-1
    turn = -1

    while left < right:
        mid = (left + right) // 2
        if (turn == -1 or turn == 0) and lst[mid] < x:
            left = mid + 1
            turn = 1

        elif (turn == -1 or turn == 1) and lst[mid] > x:
            right = mid - 1
            turn = 0

        elif lst[mid] == x:
            break
        else:
            return False

    return True


for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for b in B:
        if b in A and binarySearch(A, b):
            cnt += 1
    print('#{} {}'.format(tc, cnt))