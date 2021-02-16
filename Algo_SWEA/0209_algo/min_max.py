T = int(input())
def maxL(lst):
    maxV = lst[0]
    for l in lst:
        if l > maxV:
            maxV = l
    return maxV

def minL(lst):
    minV = lst[0]
    for l in lst:
        if l < minV:
            minV = l

    return minV

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    max_element = maxL(lst)
    min_element = minL(lst)
    result = max_element - min_element
    print(f'#{t} {result}')