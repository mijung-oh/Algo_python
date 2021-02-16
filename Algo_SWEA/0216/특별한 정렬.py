T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 입력 받은 배열을 sort 시킨다
    arr.sort()
    result = []
    l = 0
    r = len(arr)-1
    while 1:
        result.append(arr[r])
        result.append(arr[l])
        l += 1
        r -= 1
        # r이 l과 같거나 l보다 작아지면 멈춘다
        if r <= l:
            break
    print(f'#{t}')
    for r in range(10):
        print(result[r], end=' ')
    print()