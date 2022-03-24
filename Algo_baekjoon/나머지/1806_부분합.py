import sys
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

subSum = 0
minLen = sys.maxsize

l = r = 0
while True:
    # 만약 합이 S보다 크면
    if subSum >= S:
        minLen = min(minLen, r-l)
        # 더 작은 길이가 있나 확인하기 위해 맨 왼쪽값을 subSum에서 뺀다.
        subSum -= numbers[l]
        # left 를 +1 해준다.
        l += 1
    elif r == N:
        break
    # 만약 S보다 작으면
    elif subSum < S:
        subSum += numbers[r]
        r += 1
print(minLen if minLen != sys.maxsize else 0)
