T = int(input())

def tr(root):
    global cnt
    if root:
        cnt += 1
        tr(Tree[root][0])
        tr(Tree[root][1])

for tc in range(1, T+1):
    E, N = map(int, input().split())
    # 노드 개수만큼 리스트 만들기
    Tree = [[0,0] for _ in range(E+2)]
    lst = list(map(int, input().split()))

    for i in range(0, len(lst), 2):
        p = lst[i]
        c = lst[i+1]
        if Tree[p][0] == 0:
            Tree[p][0] = c
        else:
            Tree[p][1] = c

    cnt = 0
    tr(N)
    print('#{} {}'.format(tc, cnt))