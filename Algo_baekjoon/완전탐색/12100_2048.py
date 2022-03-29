from collections import deque

# 위로 이동
def up(brd):
    for i in range(len(brd[0])):
        t = deque()
        for j in range(len(brd)):
            if brd[j][i]: t.append(brd[j][i])
        # t change
        new_t = []
        while t:
            if len(t) >= 2:
                x = t.popleft()
                y = t.popleft()
                if x == y:
                    new_t.append(x+y)
                else:
                    new_t.append(x)
                    t.appendleft(y)
            else:
                x = t.popleft()
                if x: new_t.append(x)
        # 다시 brd에 저장
        for j in range(len(brd)):
            if j < len(new_t):
                brd[j][i] = new_t[j]
            else:
                brd[j][i] = 0
    return brd


# 아래로 이동
def down(brd):
    for i in range(len(brd[0])):
        t = deque()
        for j in range(len(brd)-1, -1, -1):
            if brd[j][i]: t.append(brd[j][i])
        # t change
        new_t = deque()
        while t:
            if len(t) >= 2:
                x = t.popleft()
                y = t.popleft()
                if x == y:
                    new_t.append(x+y)
                else:
                    new_t.append(x)
                    t.appendleft(y)
            else:
                x = t.popleft()
                if x: new_t.append(x)
        # 다시 brd에 저장
        for j in range(len(brd)-1, -1, -1):
            if new_t:
                brd[j][i] = new_t.popleft()
            else:
                brd[j][i] = 0
    return brd

# 왼쪽 이동
def left(brd):
    for i in range(len(brd)):
        t = deque()
        for j in range(len(brd[i])):
            if brd[i][j]: t.append(brd[i][j])
        # t change
        new_t = deque()
        while t:
            if len(t) >= 2:
                x = t.popleft()
                y = t.popleft()
                if x == y:
                    new_t.append(x+y)
                else:
                    new_t.append(x)
                    t.appendleft(y)
            else:
                x = t.popleft()
                if x: new_t.append(x)
        # 다시 brd에 저장
        for j in range(len(brd)):
            if new_t:
                brd[i][j] = new_t.popleft()
            else:
                brd[i][j] = 0
    return brd

# 오른쪽 이동
def right(brd):
    for i in range(len(brd)):
        t = deque()
        for j in range(len(brd[i])-1, -1, -1):
            if brd[i][j]: t.append(brd[i][j])
        # t change
        new_t = deque()
        while t:
            if len(t) >= 2:
                x = t.popleft()
                y = t.popleft()
                if x == y:
                    new_t.append(x+y)
                else:
                    new_t.append(x)
                    t.appendleft(y)
            else:
                x = t.popleft()
                if x: new_t.append(x)
        # 다시 brd에 저장
        for j in range(len(brd)-1, -1, -1):
            if new_t:
                brd[i][j] = new_t.popleft()
            else:
                brd[i][j] = 0
    return brd

result = -1
def f(cnt, brd):
    global result
    if cnt > 5:
        # 최대 블록 저장
        for i in range(len(brd)):
            result = max(result, max(brd[i]))
        return
    f(cnt+1, up(brd))
    f(cnt+1, right(brd))
    f(cnt+1, down(brd))
    f(cnt+1, left(brd))

N = int(input())
BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))
f(0, BRD)
print(result)

