T = int(input())

# 그냥 숫자로 접근하기. 0 생각 노노
BRD = [[0 for _ in range(101)] for _ in range(101)]
for tc in range(T):
    # left: y축, botton: x축
    left, bottom = map(int, input().split())
    # 1로 색칠하기.
    for i in range(bottom, bottom+10):
        for j in range(left, left+10):
            BRD[i][100-j] = 1 

# 하나의 변을 탐색하면서
# 길이가 같은것의 반복이면 계속 그 값을 더해준다.
# 만약 길이가 달라지면 그 전의 값은 초기화하고 다시 시작한다.

# y축 먼저 탐색
max_area = 0
for x in range(1, 101):
    pre_row = 0
    total = 0
    for y in range(1, 101):
        if BRD[x][y]:
            # 가로길이 구하기.
            row_len = 0
            for l in range(100):
                if x+l > 100: break
                if BRD[x+l][y]:
                    row_len += 1
            if pre_row == row_len:
                total += row_len
            else:
                if max_area < total:
                    max_area = total
                total = pre_row = row_len
        # 빈 부분인 경우 pre row 초기화
        else:
            pre_row = 0
    if max_area < total:
        max_area = total

# x축 탐색
for y in range(1, 101):
    pre_col = 0
    total = 0
    for x in range(1, 101):
        if BRD[x][y]:
            # 가로길이 구하기.
            col_len = 0
            for l in range(100):
                if y+l>100: break
                if BRD[x][y+l]:
                    col_len += 1
            if pre_col == col_len:
                total += col_len
            else:
                if max_area < total:
                    max_area = total
                total = pre_col = col_len
        # 빈 부분인 경우 pre row 초기화
        else:
            pre_col = 0
    if max_area < total:
        max_area = total
                

print(max_area)