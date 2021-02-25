T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 복도 배열
    # 지나가는 부분을 +1 해준다
    # 배열의 최대값이  필요한 시간이 된다.
    hall = [0]*201
    for n in range(N):
        st, goal = map(int, input().split())
        # 만약 시작점이 끝점보다 큰 값일 경우 순서를 바꿔준다!
        if st > goal:
            st, goal = goal, st
        # 홀수인 경우
        # 1-> 0번인덱스, 2->0번인덱스이기 때문에 홀수일 경우는 각각 +1을 해줘서 짝수로 맞춰준다.
        if st%2:
            st += 1
        if goal%2:
            goal += 1
        for i in range(st, goal+1, 2):
            hall[i//2] += 1
    print('#{} {}'.format(tc, max(hall)))

