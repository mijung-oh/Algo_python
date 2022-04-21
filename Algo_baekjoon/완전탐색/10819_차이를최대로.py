import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

############## 완전 탐색 ##################

# 사이합 구하는 함수
def sumGap(a):
    s = 0
    for i in range(1, len(a)):
        s += abs(a[i] - a[i-1])
    return s
result = -1
for p in permutations(arr, len(arr)):
    result = max(result, sumGap(p))
print(result)
