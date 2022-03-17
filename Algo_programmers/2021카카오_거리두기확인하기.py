def checkCross(brd):
    # 중복으로 확인하지 않도록
    visited = [[0 for _ in range(5)] for _ in range(5)]
    
    # 본인이 p 인 경우 대각선이 p인 부분이 있는지 탐색
    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j] == 'P':
                # 대각선 탐색
                for d in [(-1,-1), (-1,1), (1, -1), (1, 1)]:
                    if 0 <= i + d[0] < 5 and 0 <= j + d[1] < 5 and brd[i+d[0]][j+d[1]] == 'P':
                        visited[i+d[0]][j+d[1]] = 1
                        # 있다면 그로부터 주변을 탐색
                        # 둘 중 하나라도 O이면 return False
                        if brd[i][j+d[1]] == 'O' or brd[i][j+d[1]] == 'P' or brd[i+d[0]][j] == 'O' or brd[i+d[0]][j] == 'P':
                            return False
                        
    return True

def checkFourD(brd):
    # 중복으로 확인하지 않도록
    visited = [[0 for _ in range(5)] for _ in range(5)]

    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j] == 'P':
                # 상하좌우 2칸차이 탐색
                for d in [(-2, 0), (2, 0), (0, 2), (0, -2)]:
                    if 0 <= i + d[0] < 5 and 0 <= j + d[1] < 5 and brd[i+d[0]][j+d[1]] == 'P':
                        visited[i+d[0]][j+d[1]] = 1
                        if brd[i + d[0]//2][j + d[1]//2] == 'O' or brd[i + d[0]//2][j + d[1]//2] == 'P':
                            return False
    return True

def solution(places):
    answer = []
    for place in places:
        # 대각선 확인하기
        first = checkCross(place)

        # 상하좌우 2칸 확인하기
        second = checkFourD(place)

        if first and second:
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))