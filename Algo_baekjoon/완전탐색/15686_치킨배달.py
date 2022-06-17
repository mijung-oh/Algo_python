import sys
from itertools import combinations
N, C = map(int, input().split())
BRD = [list(map(int, input().split())) for _ in range(N)]
MAX_DIST = sys.maxsize

# 치킨집, 집 위치 저장
chicken = []
house = []
for r in range(N):
    for c in range(N):
        if BRD[r][c] == 2:
            chicken.append((r,c))
        elif BRD[r][c] == 1:
            house.append((r,c))

answer = sys.maxsize
visited = [0 for _ in range(len(chicken))]
for combi in combinations(chicken, C):
    total = 0
    for h in house:
        dist = MAX_DIST
        for ch in combi:
            # 치킨집을 돌면서 가장 가까운 집의 거리를 구한다.
            if abs(ch[0]-h[0]) + abs(ch[1]-h[1]) < dist:
                dist = abs(ch[0]-h[0]) + abs(ch[1]-h[1])
        total += dist
    answer = min(answer, total)
print(answer)
