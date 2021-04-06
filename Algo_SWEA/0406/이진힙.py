T = int(input())


def tr(idx):
    global N
    if 1 <= idx:
        if idx//2 >= 1 and lst[idx] < lst[idx//2]:
            lst[idx], lst[idx//2] = lst[idx//2], lst[idx]
        tr(idx // 2)
    return

for tc in range(1, T+1):
    N = int(input())

    lst = [0]
    V = list(map(int, input().split()))

    for data in V:
        lst.append(data)
        tr(len(lst)-1)
    result = 0

    p = len(lst)-1
    while p > 1:
        p //= 2
        result += lst[p]

    print(lst)
    print('#{} {}'.format(tc, result))
