N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 시간초과 코드
# 연속된 합이 M이 되면 cnt += 1
cnt = 0
for i in range(N):
    subSum = 0
    for j in range(i, N):
        subSum += numbers[j]
        if subSum == M:
            cnt += 1
            break
        elif subSum > M:
            break
print(cnt)


# 투 포인터로 접근
l = r = 0
cnt = 0
while l<=r and r<N:
    subSum = sum(numbers[l:r+1])
    
    # 만약 합이 M보다 작으면 r+1
    if subSum < M: r += 1
    # M과 같으면 l+1, r=l
    # M보다 크면 l += 1하고 r도 같이 초기화
    elif subSum == M: 
        l += 1
        r = l
        cnt += 1
    elif subSum > M:
        l += 1
        r = l
        
print(cnt)