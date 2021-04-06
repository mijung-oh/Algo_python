T = int(input())

for tc in range(1, T+1):
    node, leaf, target = map(int, input().split())
    G = [0]*( node + 1 )

    for _ in range(leaf):
        leaf_number, leaf_value = map(int, input().split())
        G[leaf_number] = leaf_value

    # G를 뒤에서부터 순회하면서
    # 항상 왼쪽은 짝수 오른쪽은 홀수
    # 바로 인덱스가 짝수라면
    # 바로 부모로 보내줌
    # 홀수라면 -1 인덱스의 합을 부모로 보내줌

    current = len(G)-1
    while current // 2 >= 1:
        # 홀수라면
        if current % 2:
            G[current//2] = G[current] + G[current-1]
            current -= 2
        else:
            G[current // 2] = G[current]
            current -= 1
    print('#{} {}'.format(tc, G[target]))