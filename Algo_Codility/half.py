# O(N*log(N)) or O(N) or O(N**2)
# 83% timeout 발생
def solution(A):
    half = len(A) / 2
    visit = []
    for idx, a in enumerate(A):
        if a in visit:
            continue
        visit.append(a)
        if A.count(a) > half:
            return idx
    return -1

# O(N*log(N)) or O(N)
def solution(A):
    half = len(A) / 2
    d = {}
    for idx, a in enumerate(A):
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
        if d[a] > half:
            return idx
    return -1
