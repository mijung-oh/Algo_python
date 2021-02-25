T = int(input())

for t in range(1, T+1):
    # A와 B사이 거리, A속력, B속력, 파리속력
    G, A, B, P = map(int, input().split())
    # 1. A와 B 가 몇시간 지났을 때 충돌하는지 구하기
    time = G / (A+B)
    result = P*time
    print('#{} {:0.10f}'.format(t, result))