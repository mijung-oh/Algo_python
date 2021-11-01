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
        c.append(L)
    else:
        r.append(L)
# 끝점 추가
r.append(row)
c.append(col)
# 정렬
r.sort()
c.sort()
# 길이 모음
r2 = []
c2 = []
for i in range(1,len(r)):
    r2.append(abs(r[i]-r[i-1]))
for i in range(1,len(c)):
    c2.append(abs(c[i]-c[i-1]))

# 넓이 모음
area = []
for i in range(len(r2)):
    for j in range(len(c2)):
        area.append(r2[i]*c2[j])
print(max(area))

