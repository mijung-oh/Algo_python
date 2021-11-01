N, B = map(int, input().split())

BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        BRD[i][j] %= 1000

def mulfor(a, b):
    N = len(b)
    M = len(b[0])
    result= [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]
    return result
            

# 행렬 a와 b의 곱셈
def mulMatrix(a, b):
    global N
    result = []
    for i in range(len(a)):
        for j in range(len(a)):
            r = a[i]
            c = [k[j] for k in b]
            total = 0
            for l in range(len(a)):
                total += r[l] * c[l]
            result.append(total % 1000)
    result2 = []
    for i in range(0, len(result), N):
        result2.append(result[i:i+N])
    return result2

def check(M, b):
    if b == 1:
        return M
    elif b%2:
        return mulfor(check(M, b-1), check(M, 1))
    else:
        t = check(M, b//2)
        return mulfor(t,t)


total = check(BRD,B)

for i in range(len(total)):
    for j in range(len(total)):
        print(total[i][j], end=' ')
    print()