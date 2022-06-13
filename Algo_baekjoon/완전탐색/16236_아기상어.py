# NxN 크기 물고기 M마리 상어 1마리
# 처음 상어 크기는 2이고 자기보다 큰 물고기가 있는 칸은 못감
# 크기가 같으면 지나갈수만 있음
# 크기가 작으면 먹을수도 있음
# 먹을 수 있는 고기가 1마리라면 바로 직진
# 1마리보다 많으면 거리가 가장 가까운 걸로
# 거리가 가까운게 많다면 가장 위+왼쪽에 있는 물고기로

N = int(input())
BRD = [list(map(int, input().split())) for _ in range(N)]

# 상어 위치 찾기
st = 0
for r in range(N):
    for c in range(N):
        if BRD[r][c] == 9:
            st = (r,c)
            break
    if st: break

# 소요시간
time = 0
