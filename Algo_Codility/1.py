def solution(A):
    arr = []
    for i, v in enumerate(A):
        arr.append((i-v, -1))
        arr.append((i+v, 1))

    arr.sort()
    intersection = 0
    intervals = 0
    print(arr)
    for v in arr:
        if v[1] == 1 :
            intervals -= 1
        if v[1] == -1:
            print(intervals)
            intersection += intervals
            intervals += 1
    if intersection > 10000000:
        intersection = -1

    return intersection

solution([1, 5, 2, 1, 4, 0])


# 시간초과
    # intersect = []
    # for i in range(N):
    #     # i = 0,1,2,3,4
    #     # j = i+1 ~ N-1
    #     for j in range(i+1, N):
    #         dist = abs(j - i)
    #         r1 = A[i]
    #         r2 = A[j]
    #         if dist < r1 + r2:
    #             intersect.append((i,j))
    # print(intersect)
