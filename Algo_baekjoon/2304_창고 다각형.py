N = int(input())
lst = []
BRD = [[0 for x in range(1001)] for y in range(1001)]

for n in range(N):
    a = tuple(map(int, input().split()))
    lst.append(a)
lst.sort()
# print(max(lst[2:]))
max_height = 0
for i in range(len(lst)):
    check = 0
    # next_h = lst[i+1][1]
    # 자기 다음부터 더 높은 기둥이 있는지 확인
    for j in range(i+1, len(lst)):
        if max_height < lst[j][1]:
            next = lst[j]
            print('같은 경우', next)
            check = 1
            break
    # 더 높은 기둥이 없는 경우 두 번째로 높은 기둥을 다음껄로 잡는다.
    # i번째 다음의 원소들 중 가장 큰 원소를 찾는다.
    if check == 0:
        max_ele = -1
        for k in range(i+1, len(lst)):
            if max_ele < lst[k][1]:
                max_idx = k
                max_ele = lst[k][1]
        next = (k, max_ele)
        print('다른 경우', next)
    max_idx = next[0]
    max_height = next[1]
    # 1로 넓이를 채워준다.
    for x in range(lst[i][0],next[0]):
        for y in range(0, lst[i][1]+1):
            BRD[x][y] = 1

for i in range(15):
    for j in range(20):
        print(BRD[i][j], end='')
    print()