import sys
input = sys.stdin.readline
N, M = map(int, input().split())
sel = [0]*M
arr = list(range(1, N+1))

def isNotdec(lst):
    for i in range(1, len(lst)):
        if lst[i-1] <= lst[i]:
            continue
        else:
            return False
    return True


def powerset(k,N, M):
    if k == M:
        if isNotdec(sel):
            print(*sel)
        return

    for i in range(N):
        sel[k] = arr[i]
        powerset(k+1, N, M)

powerset(0, N, M)