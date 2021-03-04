T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    q = list(map(int, input().split()))

    for i in range(int(M)):
        q.append((q.pop(0)))
    print('#{} {}'.format(tc, q[0]))
