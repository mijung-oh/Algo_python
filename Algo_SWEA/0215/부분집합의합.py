T = int(input())

def isZero(n, k, arr):
    count = 0
    for i in range(1<<12):
        sumV = 0
        total = 0
        for j in range(12):
            if i & (1<<j):
                total += 1
                sumV += arr[j]
        if sumV == k and total == n:
            print(total)
            count += 1
    return count

for t in range(1 , T+1):
    arr = []
    N, K = map(int, input().split())
    for n in range(1, 13):
        arr.append(n)
    c = isZero(N, K, arr)
    print(f'#{t} {c}')
