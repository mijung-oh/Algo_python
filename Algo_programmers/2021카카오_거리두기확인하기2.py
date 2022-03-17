# 본인이 P인 경우 상하좌우에 P가 있다면 False
def selfP(brd):
    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j] == 'P':
                for d in [(1,0), (0,1), (-1,0), (0,-1)]:
                    if 0 <= i + d[0] < len(brd) and 0 <= j + d[1] < len(brd[0]) and brd[i+d[0]][j+d[1]] == 'P':
                        return False
    return True

# 본인이 O인 경우 상하좌우에 P가 2개 이상이면 False
def selfO(brd):
    check = 0
    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j] == 'O':
                for d in [(1,0), (0,1), (-1,0), (0,-1)]:
                    if 0 <= i + d[0] < len(brd) and 0 <= j + d[1] < len(brd[0]) and brd[i+d[0]][j+d[1]] == 'P':
                        check += 1
                        if check >= 2:
                            return False
            check = 0

    return True



def solution(places):
    answer = []

    for place in places:
        res1 = selfP(place)
        res2 = selfO(place)
        print(res1, res2)
        if res1 and res2:
            answer.append(1)
        else:
            answer.append(0)


    
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))