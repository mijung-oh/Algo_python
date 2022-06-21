import copy
from collections import deque

N = int(input())
BRD = [list(map(int, input().split())) for _ in range(N)]

# 가장 큰 블록의 값
result = -1

# 위로 이동
def up(brd):
    for c in range(len(brd[0])):
        t = deque()
        for r in range(len(brd)):
            t.append((brd[r][c], 0))
        l = len(t)

        # 현재 원소와 다음에 나오는 원소가 같을 경우
        pre = 0
        while t:
            if t[0][1] == 1:
                break
            cur = t.popleft()
            if cur[0] == 0:
                continue
            if pre == 0 and cur[0]:
                pre = cur[0]
            elif pre and pre == cur[0]:
                t.append((pre+cur[0], 1))
                pre = 0
            elif pre and pre != cur[0]:
                t.append((pre, 1))
                pre = cur[0]
        # 마지막 원소
        if pre:
            t.append((pre, 1))
        # 원래 길이만큼 0을 채워준다.
        for _ in range(l-len(t)):
            t.append((0,0))

        # brd 업데이트
        for r in range(len(brd)):
            brd[r][c] = t[r][0]
    return brd

# 아래로 이동
def down(brd):
    for c in range(len(brd[0])):
        t = deque()
        for r in range(len(brd)):
            t.append((brd[r][c], 0))
        l = len(t)

        # 현재 원소와 다음에 나오는 원소가 같을 경우
        pre = 0
        while t:
            if t[-1][1] == 1:
                break
            cur = t.pop()
            if cur[0] == 0:
                continue
            if pre == 0 and cur[0]:
                pre = cur[0]
            elif pre and pre == cur[0]:
                t.appendleft((pre+cur[0], 1))
                pre = 0
            elif pre and pre != cur[0]:
                t.appendleft((pre, 1))
                pre = cur[0]
        # 마지막 원소
        if pre:
            t.appendleft((pre, 1))
        # 원래 길이만큼 0을 채워준다.
        for _ in range(l-len(t)):
            t.appendleft((0,0))

        # brd 업데이트
        for r in range(len(brd)):
            brd[r][c] = t[r][0]
    return brd

# 오른쪽으로 이동
def right(brd):
    for r in range(len(brd)):
        t = deque()
        for c in range(len(brd)):
            t.append((brd[r][c], 0))
        l = len(t)

        # 현재 원소와 다음에 나오는 원소가 같을 경우
        pre = 0
        while t:
            if t[-1][1] == 1:
                break
            cur = t.pop()
            if cur[0] == 0:
                continue
            if pre == 0 and cur[0]:
                pre = cur[0]
            elif pre and pre == cur[0]:
                t.appendleft((pre+cur[0], 1))
                pre = 0
            elif pre and pre != cur[0]:
                t.appendleft((pre, 1))
                pre = cur[0]
        # 마지막 원소
        if pre:
            t.appendleft((pre, 1))
        # 원래 길이만큼 0을 채워준다.
        for _ in range(l-len(t)):
            t.appendleft((0,0))

        # brd 업데이트
        for c in range(len(brd)):
            brd[r][c] = t[c][0]
    return brd

# 왼쪽으로 이동
def left(brd):
    for r in range(len(brd)):
        t = deque()
        for c in range(len(brd)):
            t.append((brd[r][c], 0))
        l = len(t)

        # 현재 원소와 다음에 나오는 원소가 같을 경우
        pre = 0
        while t:
            if t[0][1] == 1:
                break
            cur = t.popleft()
            if cur[0] == 0:
                continue
            if pre == 0 and cur[0]:
                pre = cur[0]
            elif pre and pre == cur[0]:
                t.append((pre+cur[0], 1))
                pre = 0
            elif pre and pre != cur[0]:
                t.append((pre, 1))
                pre = cur[0]
        # 마지막 원소
        if pre:
            t.append((pre, 1))
        # 원래 길이만큼 0을 채워준다.
        for _ in range(l-len(t)):
            t.append((0,0))

        # brd 업데이트
        for c in range(len(brd)):
            brd[r][c] = t[c][0]
    return brd

# 이동 함수 di: 방향, cnt: 이동 횟수
def move(cnt, brd):
    global result, N
    if cnt > 5:
        return
    
    # 가장 큰 값 찾기
    for i in range(N):
        for j in range(N):
            if brd[i][j] > result:
                result = brd[i][j]
    NEWBRD = [item[:] for item in brd]
    move(cnt+1, right(NEWBRD))

    NEWBRD = [item[:] for item in brd]
    move(cnt+1, down(NEWBRD))

    NEWBRD = [item[:] for item in brd]
    move(cnt+1, up(NEWBRD))

    NEWBRD = [item[:] for item in brd]
    move(cnt+1, left(NEWBRD))

    return

move(0, BRD)
print(result)
