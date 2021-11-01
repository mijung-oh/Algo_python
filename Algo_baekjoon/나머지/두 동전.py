from collections import deque
rows, cols = map(int, input().split())
BRD = []

for i in range(rows):
    BRD.append(list(input()))

# 두 동전 위치 구하기
coins = []
for i in range(rows):
    for j in range(cols):
        if BRD[i][j] == 'o':
            coins.append(i)
            coins.append(j)
        
        if len(coins) == 4: break
    if len(coins) == 4: break

loc = deque()
loc.append((coins[0], coins[1], coins[2], coins[3], 0))

minV = 11
while loc:
    r1, c1, r2, c2, cnt = loc.popleft()
    for r in [(1,0), (0,1), (-1,0), (0,-1)]:
        
        # print('pre', r1, c1, r2, c2)
        # 두 개의 동전 이동
        nr1 = r1 + r[0]
        nr2 = r2 + r[0]
        nc1 = c1 + r[1]
        nc2 = c2 + r[1]
        if cnt > 10:
            continue
        
        # 두 개의 동전이 모두 안 떨어진 경우
        if 0 <= nr1 < rows and 0 <= nc1 < cols and 0 <= nr2 < rows and 0 <= nc2 < cols:
            # 다음 위치가 벽인 경우는 위치 그대로
            if BRD[nr1][nc1] == '#':
                nr1 = r1
                nc1 = c1
            if BRD[nr2][nc2] == '#':
                nr2 = r2
                nc2 = c2
            # print(nr1, nc1, nr2, nc2)
            loc.append((nr1,nc1,nr2,nc2,cnt + 1))
        
        # 한 개의 동전만 떨어진 경우
        elif ((0 <= nr1 < rows and 0 <= nc1 < cols) and (nr2 < 0 or nr2 >= rows or nc2 < 0 or nc2 >= cols)) \
                or ((0 <= nr2 < rows and 0 <= nc2 < cols) and (nr1 < 0 or nr1 >= rows or nc1 < 0 or nc1 >= cols)):
                if minV > cnt + 1:
                    minV = cnt + 1
        # 두 개의 동전이 모두 떨어진 경우 실패!

        # print(nr1, nc1, nr2, nc2, cnt)
        

if minV == 11:
    print("-1")
else:
    print(minV)