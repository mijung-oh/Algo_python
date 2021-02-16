import sys
input() = sys.sys.stdin.readline()

T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())

    result = [0]*(N+1)
    
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            result[i] = q
    
    print(f'#{t}', end=' ')
    for r in range(1, N+1):
        print(result[r], end=' ')
    print()

    