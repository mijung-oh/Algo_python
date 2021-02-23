T = int(input())

for i in range(T):
    total = 0
    O_score = 0

    ox = input()
    for element in ox:
        if element == 'O':
            O_score += 1
            total += O_score
        else:
            O_score = 0

    print(total)
