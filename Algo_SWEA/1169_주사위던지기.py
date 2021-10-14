N, M = map(int, input().split())
lst = [0] * N
used = [0] * 7

# 주사위: 1~6
def run1(lev):
    if lev == N:
        print(lst)
        return
    
    for i in range(1, 7):
        lst[lev] = i
        run1(lev+1, lst)

def run2(lev, start):
    if lev == N:
        print(lst)
        return
    
    for i in range(start, 7):
        lst[lev] = i
        run2(lev+1, i)

def run3(lev):
    if lev == N:
        print(lst)
        return
    for i in range(1, 7):
        if not used[i]:
            used[i] = 1
            lst[lev] = i
            run3(lev+1)
            used[i] = 0


if M == 1:
    run1(0)
if M == 2:
    run2(0, 1)
if M == 3:
    run3(0)
    