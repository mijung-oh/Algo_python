T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A=[]
    B=[]
    # A, B 에 값 넣기
    for n in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # P개의 버스정류장 번호 받기
    P = int(input())
    bus_stop = []
    for p in range(P):
        bus_stop.append(int(input()))

    # 5000개의 버스정류장 (1~5000)
    bus_count = [0]*5001

    # A[n]~B[n] 인 버스정류장 ++해주기
    for n in range(N):
        for i in range(A[n], B[n]+1):
            bus_count[i] +=1
        
    print(f'#{tc}', end=' ')
    for bus in bus_stop:
        print(bus_count[bus], end=' ')

    print()