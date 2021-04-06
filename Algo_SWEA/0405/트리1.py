for t in range(1, 11):
    N = int(input())
    lst = []
    for i in range(N):
        a = list(input().split())
        lst.append(a[1:])

    print(lst)
    result = ''
    def search(x):
        global result
        # 왼쪽 아래 노드
        if len(lst[x]) >= 2:
            search(int(lst[x][1])-1)
        # 부모
        result += lst[x][0]
        # 오른쪽 아래 노드
        if len(lst[x]) >= 3:
            search(int(lst[x][2])-1)

    search(0)
    print('#{} {}'.format(t, result))