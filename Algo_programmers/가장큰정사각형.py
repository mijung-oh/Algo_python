def solution(board):
    answer = 0
    # 1을 발견하면
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                # 가로로 1이 몇개인지 확인한다.
                cntRow = 0
                idx = j
                while idx < len(board[0]):
                    if board[i][idx] == 1:
                        cntRow += 1
                    idx += 1
                # cntRow가 현재 가장 큰 정사각형 변보다 작으면 pass
                if cntRow < answer: continue

                # cntRow만큼 돌면서 가장 큰 정사각형을 찾는다.
                for k in range(cntRow, answer, -1):
                    check = True
                    # 정사각형이면 answer를 바꾼다.
                    for x in range(i, i+k):
                        for y in range(j, j + k):
                            if x >= len(board) or y >= len(board[0]):
                                check = False
                                break
                            if x < len(board) and y < len(board[0]) and board[x][y] != 1:
                                check = False
                                break
                        if not check: break
                    if check: 
                        answer = k if answer < k else answer
                    
    print(answer)
    answer = answer * answer
    return answer
solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]])