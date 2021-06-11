t = int(input())


def dfs(cur, boxH, cur_x, cur_y, boxCount):
    # 최대높이 설정
    global max_box_h, box_cnt
    if max_box_h < boxH:
        max_box_h = boxH
        print('최대: ', max_box_h)

    if visited[cur] or boxCount > box_cnt:
        return

    visited[cur] = 1
    cur_r, cur_c, cur_z = box_q[cur]
    next_ = cur

    for x, y, z in [(cur_r, cur_c, cur_z), (cur_c, cur_z, cur_r), (cur_r, cur_z, cur_c)]:
        # 현재 박스의 제일 윗면이 될 가로 세로 == x,y
        # 만약 박스의 제일 윗면과 현재 박스의 밑면이 벗어나는 경우는 pass
        if boxH == 113:
            print(cur_x, x, cur_y, y, visited)
        if cur_x==0 and cur_y == 0:
            next_ = cur
        elif (cur_x >= x and cur_y >= y) or (cur_x >= y and cur_y >= x):
            # 다음 박스를 선택한 뒤
            # 재귀호출을 하여서 그 박스의 가로세로를 정한다.
            for nextBox in range(box_cnt):
                if not visited[nextBox]:
                    next_ = nextBox
                    break
                
        print(boxH, z, boxCount)
        dfs(next_, boxH + z, x, y, boxCount + 1)




for tc in range(1, t+1):
    box_cnt = int(input())
    box_q = []

    max_box_h = -1
    for box in range(box_cnt):
        r, c, z = map(int, input().split())
        box_q.append((r,c,z))

    # visited[1] = 1
    # visited = [0] * box_cnt
    # dfs(2, 0, 0, 0, 1)
    # 시작박스를 어떻게 할건지?
    for box in range(box_cnt):
        print(box_q[box])
        visited = [0] * box_cnt
        dfs(box, 0, 0, 0, 1)
        visited[box] = 0
