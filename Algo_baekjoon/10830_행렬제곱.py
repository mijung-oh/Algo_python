N, B = map(int, input().split())

BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))

def mulList(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result
   
# 주석
def mulMatrix(a, b):
    result = []
    for i in range(len(a)):
        for j in range(len(a)):
            r = a[i]
            c = [k[j] for k in b]
            result.append(mulList(r, c))
    return result

count = 1
total = BRD
while count != B:
    if count * 2 > B:
        total = mulMatrix(total, BRD)
        count += 1
    else:
        total = mulMatrix(total, total)
        count *= 2
print(total)