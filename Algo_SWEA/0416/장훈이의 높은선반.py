import sys
sys.stdin = open('선반input.txt', 'r')

def combi(n):
    gap = 0xffffffff
    for i in range(1<<n):
        total = 0
        for j in range(n):
            if i & 1<<j:
                total += height[j]
            if total >= B and total - B > gap:
                break
        if total >= B:
            if gap > total - B:
                gap = total - B
    return gap


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
  
    print('#{} {}'.format(tc, combi(N)))
