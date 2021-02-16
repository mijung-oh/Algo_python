for tc in range(10):
    t = int(input())

    number = []
    for num in range(100):
        number.append(list(map(int, input().split())))
    
    max_sum = -1
    # 행
    for i in range(100):
        if max_sum < sum(number[i]):
            max_sum = sum(number[i][:])
    # 열
    total = []
    for i in range(100):
        total.append([a[i] for a in number])
    for i in range(100):
        if max_sum < sum(total[i]):
            max_sum = sum(total[i])

    # 대각선
    total = 0
    for i in range(100):
        for j in range(100):
            if i==j:
                total += number[i][j]
    if max_sum < total:
        max_sum = total

    # 반대 대각선
    total = 0
    for i in range(100):
        total += number[100-i][i]
    if max_sum < total:
        max_sum = total

    print(f'#{t} {max_sum}')