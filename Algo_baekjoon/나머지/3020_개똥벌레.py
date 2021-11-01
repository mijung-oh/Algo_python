import sys
input = sys.stdin.readline
N, H = map(int, input().split())

# 석순 r1 종유석 r2
r1 = []
r2 = []

# k 초과 값들의 개수를 반환하기
def binarySearch(lst, x):
    left = 0
    right = len(lst)-1
    while left <= right:
        mid = (left+right) // 2
        if lst[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return len(lst) - right-1
    


for n in range(N):
    size= int(input())
    if n % 2:
        r2.append(int(size))
    else:
        # 석순일때
        r1.append(int(size))

minV = 0xffff
result_cnt = 0
r1.sort()
r2.sort()

for h in range(1, H+1): # h =  1, 2, 3, ...
    # r1배열에서 크기가 h 이상인 것들의 개수 
    s1 = binarySearch(r1, h-1)
    # 종유석중 크기가 H-h+1 이상인 것들의 개수
    s2 = binarySearch(r2, H-h)
    # s1 = s2 = 0
    # for rr in r1:
    #     if rr > h: continue
    #     s1 += 1
    # for rr in r2:
    #     if rr >= H-h+1: continue
    #     s2 += 1
    # print(s1, s2)
    if s1 + s2 < minV:
        minV = s1 + s2
        result_cnt = 1
    elif s1 + s2 == minV:
        result_cnt += 1
print(minV, result_cnt)