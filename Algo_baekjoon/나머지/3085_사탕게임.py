N = int(input())

BRD = []
for n in range(N):
    BRD.append(list(input()))

def get_max_cnt(lst):
    max_result = -1
    cur_cnt = 0
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            cur_cnt += 1
        else:
            if max_result < cur_cnt:
                max_result = cur_cnt
            cur_cnt = 0
    if max_result < cur_cnt:
                max_result = cur_cnt

    return max_result + 1

max_cnt = -1

# # 가로확인
# for r in range(N):
#     # 한개씩 위아래꺼랑 바꿔본 다음에
#     new_row = BRD[r]
#     up = down = False

#     if r == 0:
#         down = BRD[r+1]
#     elif r == N-1:
#         up = BRD[r-1]
#     else:
#         up = BRD[r-1]
#         down = BRD[r+1]

#     # 한 행의 값이 다 같은지 확인
#     check = True
#     for c in range(1, N):
#         if BRD[r][c-1] != BRD[r][c]:
#             check = False
#             break
#     if check:
#         max_cnt = N
#         break

#     for c in range(N):
#         if up and new_row[c] != up[c]:
#         # 위랑 change
#             new_row[c], up[c] = up[c], new_row[c]
#             cur_result = get_max_cnt(new_row)
#             if max_cnt < cur_result: 
#                 max_cnt = cur_result
#             new_row[c], up[c] = up[c], new_row[c]


#     for c in range(N):
#         if down and new_row[c] != down[c]:
#             # 아래랑 change
#             new_row[c], down[c] = down[c], new_row[c]
#             cur_result = get_max_cnt(new_row)
#             if max_cnt < cur_result: 
#                 max_cnt = cur_result
#             new_row[c], down[c] = down[c], new_row[c]


# 세로 확인
for c in range(N):
    # 한개씩 위아래꺼랑 바꿔본 다음에
    new_col = [BRD[i][c] for i in range(N)]
    left = right = False

    if c == 0:
        right = [BRD[i][c+1] for i in range(N)]
    elif c == N-1:
        left = [BRD[i][c-1] for i in range(N)]
    else:
        left = [BRD[i][c-1] for i in range(N)]
        right = [BRD[i][c+1] for i in range(N)]

    # 한 열의 값이 다 같은지 확인
    check = True
    for r in range(1, N):
        if BRD[r-1][c] != BRD[r][c]:
            check = False
            break
    if check:
        max_cnt = N
        break

    for r in range(N):
        if left and new_col[r] != left[r]:
            new_col[r], left[r] = left[r], new_col[r]

            cur_result = get_max_cnt(new_col)
            if max_cnt < cur_result: 
                max_cnt = cur_result

            cur_result = get_max_cnt(BRD[r])
            if max_cnt < cur_result: 
                max_cnt = cur_result

            new_col[r], left[r] = left[r], new_col[r]


    for r in range(N):
        if right and new_col[r] != right[r]:
            new_col[r], right[r] = right[r], new_col[r]
            cur_result = get_max_cnt(new_col)
            if max_cnt < cur_result: 
                max_cnt = cur_result

            cur_result = get_max_cnt(BRD[r])
            if max_cnt < cur_result: 
                max_cnt = cur_result
                
            new_col[r], right[r] = right[r], new_col[r]
    
print(max_cnt)