T = int(input())

for i in range(T):
    numbers = list(map(int, input().split()))
    numbers_count = numbers[0]
    counts = numbers[1:]

    score_list = []
    count = 0

    for c in counts:
        score_list.append(c)
    numbers_avg = sum(score_list) /numbers_count

    for c in counts:
        if c > numbers_avg:
            count += 1
    percent = (count / numbers_count) * 100
    print('{0:.3f}%'.format(percent))

