T = int(input())

def tr(idx):
    global N, value
    if idx <= N:
        tr(idx*2)
        TREE[idx] = value
        value += 1
        tr(idx*2+1)

for tc in range(1, T+1):
    N = int(input())
    TREE = [[0] for _ in range(N+1)]
    print(TREE)
    value = 1
    tr(1)
    print('#{} {} {}'.format(tc, TREE[1], TREE[N//2]))
