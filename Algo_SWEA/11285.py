import math
T = int(input())

def closer(r):
    # gap = [0, abs(200-r), abs(180-r), abs(160-r), abs(140-r), abs(120-r), abs(100-r), abs(80-r), abs(60-r), abs(40-r), abs(20-r) ]
    for p in range(11, 1, -1):
        if 20*(11-p) < r < 20*(11-p+1) or math.isclose(r, 20*(11-p+1)):
            return p-1
    return 0
    
for t in range(1, T+1):
    N = int(input())
    score = 0
    for n in range(N):
        x, y = map(int, input().split())
        r = (x**2 + y**2) ** 0.5
        p = closer(r)
        score += p

    print(f'#{t} {score}')
