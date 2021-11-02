N, M = map(int, input().split())

BRD = []
for i in range(N):
    BRD.append(list(map(int, input().split())))
# cctv의 번호에 따른 갈 수 있는 방향의 가지수를 저장한다.
#   