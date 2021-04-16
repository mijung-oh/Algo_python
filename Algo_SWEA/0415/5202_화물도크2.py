T = int(input())

max_count = 0
def choice(idx, current):
    global max_sum, max_count
    end = time[idx][0]
    for i in range(len(time)):
        if time[i][1] >= end:
            # 이미 담긴 시간이면 pass
            if time[i] in current:
                continue

            current.append(time[i])
            choice(i, current)
            if len(current) > max_count:
                max_count = len(current)
            return
            # current.pop()
    print(current)
    if len(current) > max_count:
        max_count = len(current)
    # max_count = len(current)

for tc in range(1, T+1):
    N = int(input())
    time = []
    for n in range(N):
        st, en = map(int, input().split())
        time.append((en, st))
    time.sort()
    for i in range(len(time)):
        current = [time[i]]
        choice(i, current)

    print('#{} {}'.format(tc, max_count))
    

