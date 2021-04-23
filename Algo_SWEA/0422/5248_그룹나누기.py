T = int(input())

def find(x):
    parent = x
    print(f'parent: {parent}, x: {x}')
    while P[parent] != x:
        x = P[x]
    return x
        

def union(x, y):
    # 조상노드를 찾아서 통일시켜준다.
    px = find(x)
    py = find(y)
    if px == py:
        return
    # y의 부모를 x의 부모로 바꿔준다.
    for idx, p in enumerate(P):
        if p == py:
            P[idx] = px
    return




for tc in range(1, T+1):
    N, M = map(int, input().split())
    # P[i] = i
    P = [i for i in range(N+1)]
    c = list(map(int, input().split()))

    for i in range(0, len(c), 2):
        c1, c2 = c[i], c[i+1]
        union(c1, c2)
    P = set(P)
    print('#{} {}'.format(tc, len(P)-1))

