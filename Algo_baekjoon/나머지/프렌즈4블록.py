def solution(m, n, board):
    answer = 0
    Board = []
    for i in board:
        Board.append(list(i))
    ## 겹치는거 제거하는 함수
    def remove(r, c):
        nonlocal m, n, Board, answer
        q = [(r, c, Board[r][c])]
        isRemoved = False
        while q:
            # 오른쪽, 아래, 오른쪽아래 대각선이 같을 경우 q에 넣고 본인은 0으로 초기화
            curR, curC, cur = q.pop(0)
            cnt = 1
            for d in [(0,1), (1,0), (1,1)]:
                newR = curR + d[0]
                newC = curC + d[1]
                if 0 <= newR < m and 0 <= newC < n and Board[newR][newC] == cur:
                    cnt += 1
            if cnt == 4:
                isRemove = True
                # 붙어있는 4개가 같은 경우
                for d in [(0,1), (1,0), (1,1)]:
                    newR = curR + d[0]
                    newC = curC + d[1]
                    q.append((newR, newC, Board[newR][newC]))
                    Board[newR][newC] == 0
                    answer += 1
                Board[curR][curC] == 0
                answer += 1
        return isRemoved

    ## 제거 후 원소들 내리는 함수
    def reset():
        # 열을 기준으로 위에있는 원소들을 통째로 아래로 내려준다.
        for i in range(len(Board[0])):
            # 0이 있는지 확인하고 없을 경우 pass
            isBlank = 0
            for j in range(len(Board)):
                if not Board[j][i]:
                    isBlank = 1
                    break
            if not isBlank: continue

            up = []
            check = False
            topR, topC = 0, 0
            for j in range(len(Board)):
                if not check and Board[j][i]:
                    up.append(Board[j][i])
                    Board[j][i] = 0
                elif check and Board[j][i]:
                    topR, topC = j, i
                    break
                else:
                    check = True

            # 담아둔 up배열을 topR, topC 바로 위부터 쌓아준다.
            for i in range(len(up)):
                Board[topR-i-1][topC] = up.pop()
            
    isRemove = True
    while isRemove:
        isRemove = False
        for i in range(len(Board)):
            for j in range(len(Board[0])):
                if Board[i][j]:
                    print(remove(i, j))
        reset()
        print(isRemove)
        
    return answer

solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])