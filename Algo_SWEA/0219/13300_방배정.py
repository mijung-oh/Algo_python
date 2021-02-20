N, K = map(int, input().split())

# 0~5: 1학년~6학년
# 0: 여자, 1: 남자
stu = [[0 for _ in range(2)] for _ in range(6)]

for n in range(N):
    gender, grade = map(int, input().split())
    stu[grade-1][gender] += 1

# 방 개수
count = 0
for s in stu:
    for s2 in s:
        if 0<s2<=K:
            count += 1
        else:
            while s2 > 0:
                count += 1
                s2 -= K
print(count)