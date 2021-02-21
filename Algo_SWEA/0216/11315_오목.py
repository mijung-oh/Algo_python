import sys
sys.stdin = open('오목판정.txt', 'r')

T = int(input())

def isCross(lst):
    # 정방향 a 반대방향 b
    cross_a = 0
    cross_b = 0
    for i in range(len(lst)-4):
        for j in range(len(lst)):
            if lst[i][j] == 'o' and lst[i+1][j+1] == 'o' and lst[i+2][j+2] == 'o' and lst[i+3][j+3] == 'o' and lst[i+4][j+4] == 'o':
                return True
            # if lst[i][len(lst)-j-1] == 'o' and lst[i+1][len(lst)-j-2] == 'o' and lst[i+2][len(lst)-j-3] == 'o' and lst[i+3][len(lst)-j-4] == 'o' and lst[i+4][len(lst)-j-5] == 'o':
            #     return True
            if lst[i][len(lst)-j] == 'o' and lst[i+1][len(lst)-j-1] == 'o' and lst[i+2][len(lst)-j-2] == 'o' and lst[i+3][len(lst)-j-3] == 'o' and lst[i+4][len(lst)-j-4] == 'o':
                return True


def isRow(lst):
    check = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j+4 < len(lst) and lst[i][j] == 'o' and lst[i][j+1] == 'o' and lst[i][j+2] == 'o' and lst[i][j+3] == 'o' and lst[i][j+4] == 'o':
                check = 1
                break
    if check:
        return True
    return False

def isCol(lst):
    check = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j+4 < len(lst) and lst[j][i] == 'o' and lst[j+1][i] == 'o' and lst[j+2][i] == 'o' and lst[j+3][i] == 'o' and lst[j+4][i] == 'o':
                check = 1
                break
    if check:
        return True
    return False

for tc in range(1, T+1):
    N = int(input())
    lst = []
    for i in range(N):
        t = list(input())
        lst.append(t)
    # print(lst)
    if isCross(lst) or isCol(lst) or isRow(lst):
        print('#{} YES'.format(tc))
    else: 
        print('#{} NO'.format(tc))
