N, B = map(int, input().split())

BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))
def mulList(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result%1000
   
# 행렬 a와 b의 곱셈
def mulMatrix(a, b):
    result = []
    for i in range(len(a)):
        for j in range(len(a)):
            r = a[i]
            c = [k[j] for k in b]
            result.append(mulList(r, c))
    return result

def makeMatrix(lst, n):
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i+n])
    return result

count = 1
total = BRD
while count != B:
    if count * 2 > B:
        t = mulMatrix(total, BRD)
        total = makeMatrix(t, N)
        count += 1
    else:
        t = mulMatrix(total, total)
        total = makeMatrix(t, N)
        count *= 2

for i in range(len(total)):
    for j in range(len(total)):
        print(total[i][j], end=' ')
    print()

