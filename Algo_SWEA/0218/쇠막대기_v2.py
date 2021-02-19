T = int(input())

for t in range(1, T+1):
    lst = list(input())
    count = 0
    total = 0
    i=0
    while i<len(lst):
        if lst[i] == '(':
            count += 1
        else:
            if i-1 >= 0 and lst[i-1] == '(':
                count -= 1
                total += count
            else:
                total += 1
                count -= 1
        i += 1

    print('#{} {}'.format(t, total))
