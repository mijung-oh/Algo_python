T = int(input())

for t in range(1, T+1):
    D, L, N = map(int, input().split())

    total_d = 0
    for n in range(0, N):
        total_d += D*(1+n*(L/100))
    
    print(f'#{t} {total_d}')
