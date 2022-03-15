from collections import deque
def solution(N, number):
    # N으로 계산가능한 모든 것을 해본다.

    maxV = 0
    subMaxV = 0
    # N으로만 표현할 수 있는 값들을 넣는다.
    q = deque()
    for i in range(8):
        v = 0
        for j in range(i, -1, -1):
            v += N * (10**j)
        q.append((v, i+1))
        if i == 6: subMaxV = v
        if i == 7: maxV = v
    
    countV = [10 for _ in range(maxV+1)]

    # 최대값이 5555555 * 5가 되므로
    subMaxV = subMaxV * N
    print("subMax: ", subMaxV)
    
    while q:
        curV, cnt = q.popleft()
        print(curV)
        countV[curV] = cnt

        # 계산되는 값들을 다 넣는다.
        # countV의 값이 더 작을 경우에만 초기화시킨다.
        if curV + N < subMaxV and countV[curV + N] > cnt+1 and cnt+1 < 9:
            q.append((curV + N, cnt+1))
        if curV - N < subMaxV and countV[curV - N] > cnt+1 and cnt+1 < 9:
            q.append((curV - N, cnt+1))
        if curV * N < subMaxV and countV[curV * N] > cnt+1 and cnt+1 < 9:
            q.append((curV * N, cnt+1))
        if curV // N < subMaxV and countV[curV // N] > cnt+1 and cnt+1 < 9:
            q.append((curV // N, cnt+1))


    print("result: ", countV[number])
    if countV[number] > 8:
        return -1
    return countV[number]
solution(5, 12)