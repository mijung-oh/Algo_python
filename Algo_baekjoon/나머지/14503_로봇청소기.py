BRD = []
left_d = {
    0:3, 1:0, 2:1, 3:2,
}

def dfs(cur_r, cur_c, cur_d):
    print(cur_r, cur_c, cur_d)
    # 청소하기
    if not clean[cur_r][cur_c]:
        clean[cur_r][cur_c] = 1

    back_r = clean_r = cur_r
    back_c = clean_c = cur_c
    if cur_d == 0: clean_c -= 1
    elif cur_d == 1: clean_r -= 1
    elif cur_d == 2: clean_c += 1
    elif cur_d == 3: clean_r += 1


    # 왼쪽 방향에 아직 청소하지 않은 공간 존재하면 
    # 그 방향으로 회전한 다음 한칸 전진 + 청소
    if 0 <= clean_r < N and 0 <= clean_c < M and not BRD[clean_r][clean_c] \
        and not clean[clean_r][clean_c]:
        # visited_d[cur_d] = True
        dfs(clean_r, clean_c, left_d[cur_d])
        # visited_d[cur_d] = False
     

    # 왼쪽 방향에 청소할 공간이 없다면, 
    # 그 방향으로 회전하고 2번으로 돌아간다.
    elif 0 <= clean_r < N and 0 <= clean_c < M:
        if BRD[clean_r][clean_c] or clean[clean_r][clean_c]:
            # visited_d[cur_d] = True
            dfs(cur_r, cur_c, left_d[cur_d])
            # visited_d[cur_d] = False

    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 
    # 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    is_cleaned = True
    for d in [(-1,0), (1, 0), (0,-1), (0, 1)]:
        if 0 <= cur_r + d[0] < N and 0 <= cur_c + d[1] < M:
            # 벽이 아니면서 청소가 안되어있는 경우
            if not BRD[cur_r+d[0]][cur_c+d[1]] and not clean[cur_r+d[0]][cur_c+d[1]]:
                is_cleaned = False
                break

    if is_cleaned:
        if cur_d == 0: back_r += 1
        elif cur_d == 1: back_r -= 1
        elif cur_d == 2: back_c += 1
        elif cur_d == 3: back_r += 1
        # 뒤쪽방향이 벽인 경우 작동 멈추고
        if 0 <= back_r < N and 0 <= back_c < M:
            if BRD[back_r][back_c]:
                return
            else:
            # 아닌경우, 후진하고 다시 dfs
                dfs(back_r, back_c, cur_d)

    return

# N: 가로, M: 세로
N, M = map(int, input().split())
r, c, d = map(int, input().split())
clean = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
    BRD.append(list(map(int, input().split())))

visited_d = [0] * 4
dfs(r, c, d)
print(clean)

