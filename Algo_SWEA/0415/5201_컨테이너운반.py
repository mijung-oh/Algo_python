T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)
    c = t = 0
    total = 0
    while c < len(container) and t < len(truck):
        if container[c] <= truck[t]:
            total += container[c]
            c += 1
            t += 1
        else:
            c += 1
        
    print('#{} {}'.format(tc, total))