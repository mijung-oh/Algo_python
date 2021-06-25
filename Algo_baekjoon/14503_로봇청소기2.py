BRD = []
left_d = {
    0:3, 1:0, 2:1, 3:2,
}

def dfs(cur_r, cur_c, cur_d, cnt):
    # 청소하기
    if not clean[cur_r][cur_c]:
        clean[cur_r][cur_c] = 1

    back_r = clean_r = cur_r
    back_c = clean_c = cur_c
    if cur_d == 0: clean_c -= 1
    elif cur_d == 1: clean_r -= 1
    elif cur_d == 2: clean_c += 1
    elif cur_d == 3: clean_r += 1

    if cnt == 4:
        if cur_d == 0: back_r += 1
        elif cur_d == 1: back_c -= 1
        elif cur_d == 2: back_r -= 1
        elif cur_d == 3: back_c += 1
        # 뒤쪽방향이 벽인 경우 작동 멈추고
        if 0 <= back_r < N and 0 <= back_c < M:
            if BRD[back_r][back_c]:
                return
            else:
            # 아닌경우, 후진하고 다시 dfs
                dfs(back_r, back_c, cur_d, 0)

        return

    else:
        # 왼쪽 방향에 아직 청소하지 않은 공간 존재하면 
        # 그 방향으로 회전한 다음 한칸 전진 + 청소
        if 0 <= clean_r < N and 0 <= clean_c < M and not BRD[clean_r][clean_c] \
            and not clean[clean_r][clean_c]:
            dfs(clean_r, clean_c, left_d[cur_d], cnt)
        

        # 왼쪽 방향에 청소할 공간이 없다면,
        # 그 방향으로 회전하고 2번으로 돌아간다.
        elif 0 <= clean_r < N and 0 <= clean_c < M:
            if BRD[clean_r][clean_c] or clean[clean_r][clean_c]:
                dfs(cur_r, cur_c, left_d[cur_d], cnt+1)


    return

# N: 가로, M: 세로
N, M = map(int, input().split())
r, c, d = map(int, input().split())
clean = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
    BRD.append(list(map(int, input().split())))

dfs(r, c, d, 0)
print('====== 청소한 구역 =======')
for n in range(N):
    print(*clean[n])

