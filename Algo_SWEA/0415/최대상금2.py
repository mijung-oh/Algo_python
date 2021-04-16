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


def f(lst, cnt, max_v):
    global count, change, max_V, visited
    if cnt == int(count):
        if max_V < int(''.join(map(str, lst))):
            max_V = int(''.join(map(str, lst)))
            return max_V
        else:
            return
    
    for i in range(len(change)):
        if cnt + 1 <= int(count):
            lst[change[i][0]], lst[change[i][1]] = lst[change[i][1]], lst[change[i][0]]

            cnt += 1
            if max_v <= int(''.join(map(str, lst))):
                if lst in visited:
                    continue

                visited.append(lst[::])
                print(lst)
                max_v = int(''.join(map(str, lst)))
                f(lst, cnt, max_v)
            lst[change[i][0]], lst[change[i][1]] = lst[change[i][1]], lst[change[i][0]]
            cnt -= 1
       

for tc in range(1, T+1):
    number, count = input().split()
    visited = []
    lst2 = list(map(int, number))
    max_V = 0
    change = c(len(number))
    f(lst2, 0, 0)
    print('#{} {}'.format(tc, max_V))
