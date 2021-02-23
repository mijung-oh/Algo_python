row, col = map(int, input().split())
cut = int(input())

# 가로배열 r, 세로배열 c
r = [0]
c = [0]
for cu in range(cut):
    # 방향 d, 자르는 위치 l
    D, L = map(int, input().split())
    if D == 0:
        # 가로
        r.append(L)
    else:
        c.append(L)

# 넓이 모음
area = []
for i in range(1, len(c)):
    for j in range(1, len(r)):
        area.append((c[i]-c[i-1])*(r[j]-r[j-1]))

print(c, r)
print(max(area))