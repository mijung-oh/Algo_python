import sys
sys.stdin = open('빙고input', 'r')
bingo = []
bingo_check = [[0 for x in range(5)] for y in range(5)]
# target = []

def isCross():
    count_cross1 = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                if bingo_check[i][j] == 1:
                    count_cross1 += 1
                else:
                    return False
    if count_cross1 == 5:
        return True
    return False

def isCross2():
    count_cross2 = 0
    for i in range(5):
        for j in range(5):
            if i == 4-j:
                if bingo_check[i][j] == 1:
                    count_cross2 += 1
                else:
                    return False
    if count_cross2 == 5:
        return True
    return False

def isbingo():
    count_r = count_c = 0
    # 전체 그어진 선 개수
    total = 0
    # 행
    for i in range(5):
        for j in range(5):
            if bingo_check[i][j] == 1:
                count_r += 1
        if count_r == 5:
            count_r = 0
            total += 1
        else:
            count_r = 0
    # 열
    for i in range(5):
        for j in range(5):
            if bingo_check[j][i] == 1:
                # print(i,j)
                count_c += 1
        if count_c == 5:
            count_c = 0
            total += 1
        else:
            count_c = 0

    # 대각선
    if isCross():
        total += 1
    if isCross2():
        total += 1
    return total

def isTarget(target):
    # 빙고를 돌면서 해당 숫자가 있는지 확인
    # 있다면 bingo_check 에 1을 넣어줌
    for x in range(5):
        for y in range(5):
            if bingo[x][y] == target:
                bingo_check[x][y] = 1
                return True
    return False

# 빙고 배열
for i in range(5):
    t = list(map(int, input().split()))
    bingo.append(t)

result = 0
# 사회자가 부르는 숫자
for i in range(5):
    target = list(map(int,input().split()))
    flag = 0
    for j in range(5):
        isTarget(target[j])
        result += 1
        if isbingo() >= 3:
            flag = 1
            break
    if flag:
        break
print(result)