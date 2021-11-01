K = int(input())

# 세로 값을 넣는 배열
c = []
r = []
total = []
for _ in range(6):
    D, L = map(int, input().split())
    total.append(L)
    if D == 4 or D == 3:
        # 세로
        c.append(L)
    else:
        r.append(L)
max_r = max(r)
max_c = max(c)
max_area = max_r * max_c
# 중간이 뺄 넓이를 계산

for idx, t in enumerate(total):
    if t == max_r:
        print(idx, t)
        if idx+2 >= 6:
            mid_one = total[(idx + 2)%6]
            mid_two = total[(idx + 3)%6]
        elif idx+3 >= 6:
            mid_one = total[idx + 2]
            mid_two = total[(idx + 3) % 6]
        else:
            mid_one = total[idx+2]
            mid_two = total[idx+3]
        break
minus = mid_one * mid_two
result = max_area - minus

print(result*K)

