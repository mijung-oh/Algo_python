T = int(input())
# A는 동서남북 1개씩
# B는 동서남북 2개씩
# C는 동서남북 3개씩

for tc in range(1, T+1):
    N = int(input())
    BRD = []
    for i in range(N+1):
        BRD.append(list(input()))

