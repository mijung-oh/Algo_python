from random import triangular


def solution(n):
    answer = []
    # 삼각형이 될 배열을 만들어놓는다.
    triangle = []
    for i in range(1, n+1):
        triangle.append([0 for _ in range(i)])
    
    # n n-1 n-2 . . . 1 순으로 개수가 줄어들며 배열에 추가된다.
    rIdx = cIdx = 0
    turn = 0
    count = n
    value = 1
    while 0 <= rIdx < n and 0 <= cIdx < n :
        if turn % 3== 0:
            # rIdx 증가
            for i in range(count):
                triangle[rIdx][cIdx] = value
                value += 1
                # 위치 업데이트
                rIdx += 1
        elif turn % 3 == 1:
            # cIdx 증가
            for i in range(count):
                triangle[rIdx][cIdx] = value
                value += 1
                cIdx += 1
        else:
            # rIdx-1 cIdx-1
            for i in range(count):
                triangle[rIdx][cIdx] = value
                value += 1
                rIdx -= 1
                cIdx -= 1

        turn += 1
        # 움직일 횟수 업데이트
        count -= 1
        if value >= (n)*(n+1) // 2:
            break
        print(rIdx, cIdx)
    for i in range(len(triangle)):
        print(*triangle[i])
        
    return answer
solution(4)