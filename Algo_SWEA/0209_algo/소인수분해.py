T = int(input())
 
 # 2 3 5 7 11
for t in range(1, T+1):
    N = int(input())
    
    Q = [2, 3, 5, 7, 11]
    result = [0]*5

    for idx, q in enumerate(Q):
        while 1:
            if N % q == 0:
                result[idx] += 1
                N //= q
            else:
                break

    print(f'#{t}', end=' ')
    for r in result:
        print(r, end=' ')

    print()
    