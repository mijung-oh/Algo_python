T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time = []
    for n in range(N):
        st, en = map(int, input().split())
        time.append((en, st))
    time.sort(reverse=True)
    print(time)
    end_time = time.pop()[0]
    count = 1
    while time:
        en, st = time.pop()
        if st < end_time:
            continue
        end_time = en
        count += 1

    print('#{} {}'.format(tc, count))

