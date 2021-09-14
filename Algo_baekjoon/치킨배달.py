N, M = map(int, input().split())

BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))

# 치킨집 위치와 집 위치를 저장해놓는다.
chickens = []
house = []
for i in range(N):
    for j in range(N):
        if BRD[i][j] == 2:
            chickens.append((i,j))
        elif BRD[i][j] == 1:
            house.append((i,j))


# M개의 치킨 집을 고르는 경우의 수를 구한다.
def combi(n, m):
    result = []
    for i in range(1<<n):
        t = []
        for j in range(n):
            if i & 1<<j:
                t.append(j)
                
        if len(t) == m:
            result.append(t)
    return result



min_distance = 0xffffffff
# 각각의 치킨 집을 돌면서 
for chicken in combi(len(chickens), M):
    sub_distance = 0
    # [0,1,2]
    # 각각 집을 돌면서 가까운 치킨집과의 거리를 구한다. (치킨거리)
    for h in house:
        sub_min_distance = 0xffffffff
        for c in chicken:
            dist = abs(chickens[c][0] - h[0]) + abs(chickens[c][1] - h[1])
            if sub_min_distance > dist:
                sub_min_distance = dist
        # 구한 치킨거리를 sub_distance에 더한다
        sub_distance += sub_min_distance
    
    # min_distance보다 sub_distance가 작은 경우 업데이트 해준다.
    if min_distance > sub_distance:
        min_distance = sub_distance
print(min_distance)
        
        