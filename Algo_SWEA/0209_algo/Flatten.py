
def maxL(lst):
    maxIdx = 0
    maxV = lst[0]
    for idx, l in enumerate(lst):
        if maxV < l:
            maxV = l
            maxIdx = idx

    return maxIdx

def minL(lst):
    minIdx = 0
    minV = lst[0]
    for idx, l in enumerate(lst):
        if minV > l:
            minV = l
            minIdx = idx

    return minIdx

for t in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))

    while dump:
        dump -= 1
        lst[maxL(lst)] -= 1
        lst[minL(lst)] += 1

    print(f'#{t} {lst[maxL(lst)] - lst[minL(lst)]}')