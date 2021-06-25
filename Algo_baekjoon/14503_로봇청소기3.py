BRD = []
left_d = {
    0:3, 1:0, 2:1, 3:2,
}

def dfs(cur_r, cur_c, cur_d):
    # 1. 청소하기
    if BRD[cur_r][cur_c] == 0:
        BRD[cur_r][cur_c] = 2

    back_r = left_r = cur_r
    back_c = left_c = cur_c
    if cur_d == 0: 
        left_c -= 1
        back_r += 1
    elif cur_d == 1: 
        left_r -= 1
        back_c -= 1
    elif cur_d == 2: 
        left_c += 1
        back_r -= 1
    elif cur_d == 3: 
        left_r += 1
        back_c += 1

    # 만약 네 방향 중 청소할 구역이 존재하지 않으면 바로 리턴
    check = False
    for d in [(1,0), (0,1), (-1,0), (0,-1)]:
        if BRD[cur_r + d[0]][cur_c + d[1]] == 0:
            check = True
            break

    # 2. 왼쪽 방향에 청소할 공간이 있는지 확인
    if BRD[left_r][left_c] == 0:
        dfs(left_r, left_c, left_d[cur_d])
    elif not check:
        # 뒤쪽 방향이 벽이면 return
        if BRD[back_r][back_c] == 1:
            return
        dfs(back_r, back_c, cur_d)
    elif BRD[left_r][left_c] != 0:
        dfs(cur_r, cur_c, left_d[cur_d])

    return

# N: 가로, M: 세로
N, M = map(int, input().split())
r, c, d = map(int, input().split())

for n in range(N):
    BRD.append(list(map(int, input().split())))

dfs(r, c, d)
    
result = 0
for n in range(N):
    result += BRD[n].count(2)
print(result)
