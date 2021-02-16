T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(N,M)
    A = list(map(int, input().split()))    
    B = list(map(int, input().split()))

    max_sum = -1
    if N > M:
        for i in range(N-M+1):
            compare = []
            for j in range(i, i+M):
                compare.append(A[j])
            
            total = 0
            for m in range(M):
                total += compare[m] * B[m]
            
            if max_sum < total:
                    max_sum = total
    elif N < M:
        for i in range(M-N+1):
            compare = []
            for j in range(i, i+N):
                compare.append(B[j])
            
            total = 0
            for m in range(N):
                total += compare[m] * A[m]
            
            if max_sum < total:
                    max_sum = total

    print(f'#{tc} {max_sum}')
