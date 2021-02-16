T = int(input())

for t in range(1, T+1):
    N = int(input())
    number = input()

    count = [0]*10
    for num in number:
        count[int(num)] += 1

    max_count = count[0]
    max_idx = 0
    for idx, c in enumerate(count):
        if c > max_count:
            max_count = c
            max_idx = idx
        elif c == max_count and idx > max_idx:
            max_idx = idx

    print(f'#{t} {max_idx} {max_count}')