from collections import deque

T = int(input())
# 화덕
q = deque()

for tc in range(1, T+1):
    # N은 화덕 크기, M은 피자 개수
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    # 다음 피자 번호
    nextP = 0
    # 화덕 -> 큐
    for n in range(N):
        q.append((n, pizza[n]))
        nextP += 1
    # 첫번째 바퀴
    # print(q)
    # q.append(q.popleft())
    # print(q)
    while len(q) != 1:
        p = q.popleft()
        if p[1] != 0:
            q.append((p[0], p[1]//2))
            print(q)
        else:
            if nextP < len(pizza):
                q.append((nextP, pizza[nextP]//2))
                nextP += 1
                print(q, nextP)
            print(q)
    print(q)
    print('#{} {}'.format(tc, q.pop()[0]+1))
