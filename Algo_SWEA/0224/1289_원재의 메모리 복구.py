T = int(input())

for tc in range(1, T+1):
    bitS = list(map(int, input())) # [0,0,1,1]
    pre = [0]*len(bitS) # [0,0,0,0]
    count = 0
    # bitS와 pre가 다를 때 그 인덱스부터 끝까지 값을 바꿔준다.
    for i in range(len(bitS)):
        if bitS[i] != pre[i]:
            # 그 인덱스부터 끝까지 값을 바꿔줌
            for j in range(i, len(pre)):
                pre[j] = bitS[i]
            count += 1
            if pre == bitS:
                print('#{} {}'.format(tc, count))
