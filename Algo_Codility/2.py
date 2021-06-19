def combi(n):
    result = []
    for i in range(1 << n):
        t = []
        for j in range(n):
            if i & (1<<j):
                t.append(j)
        if len(t) == 3:
            result.append(t)
    return result


def solution(A):
    A.sort()
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])
    
solution([-3, 1, 2, -2, 5, 6])