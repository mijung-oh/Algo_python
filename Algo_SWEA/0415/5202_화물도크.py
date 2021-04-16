T = int(input())

max_count = 0
def choice(idx, current):
    global max_sum, max_count
    end = time[idx][1]
    for i in range(idx+1, len(time)):
        if time[i][0] >= end:
            current.append(time[i])
            choice(i, current)
            current.pop()
    total = 0
    print(current)
    for i in current:
        total += i[1]-i[0]
    if len(current) > max_count:
        max_count = len(current)

for tc in range(1, T+1):
    N = int(input())
    time = []
    for n in range(N):
        st, en = map(int, input().split())
        time.append((st,en))
    time.sort()
    for i in range(len(time)):
        current = [time[i]]
        choice(i, current)

    print('#{} {}'.format(tc, max_count))
    

