T = int(input())

def isZero(n, k, arr):
    count = 0
    for i in range(1<<12): # i: 0~2^12-1
        sumV = 0
        total = 0
        for j in range(12): # j: 0~11
            if i & (1<<j): # 1<<j: 1,2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048
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
