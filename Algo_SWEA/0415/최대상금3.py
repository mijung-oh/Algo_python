# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

def c(n):
    change = []
    for i in range(1<<n):
        a = []
        for j in range(n):
            if i & 1<<j:
                a.append(j)
        if len(a) == 2:
            change.append((a[0], a[1]))
    return sorted(change)


def f(lst, cnt, max_V):
    global count, change, odd_set, even_set
    if cnt == count:
        if max_V < int(''.join(map(str, lst))):
            max_V = int(''.join(map(str, lst)))
        return max_V
    for i in range(len(change)):
        lst3 = list(lst)
        lst3[change[i][0]], lst3[change[i][1]] = lst3[change[i][1]], lst3[change[i][0]]
        if cnt % 2:
            print(odd_set)
            if lst3 not in odd_set:
                odd_set.append(lst3)
                max_V = f(lst3, cnt+1, max_V)

                if count % 2:
                    max_V = f(lst3, count, max_V)
        else:
            if lst3 not in even_set:
                even_set.append(lst3)
                max_V = f(lst3, cnt+1, max_V)
                
                if not count % 2:
                    max_V = f(lst3, count, max_V)
    return max_V

for tc in range(1, T+1):
    odd_set = []
    even_set = []

    number, count = input().split()
    count = int(count)
    lst2 = list(map(int, number))
    change = c(len(number))
    max_V = f(lst2, 0, -1)
    print('#{} {}'.format(tc, max_V))