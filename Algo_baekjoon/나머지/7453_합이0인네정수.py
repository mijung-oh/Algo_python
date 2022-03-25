import sys
input = sys.stdin.readline
N = int(input())
A, B, C, D = [], [], [], []
cnt = 0

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a); B.append(b); C.append(c); D.append(d)

# A+B
a_b_sum = dict()
for a in A:
    for b in B:
        a_b_sum[a+b] = a_b_sum.get(a+b, 0) + 1

# C+D
for c in C:
    for d in D:
        # 만약 c+d에 부호 반대한 것이 a_b_sum에 있다면
        # 그 수만큼 cnt에 더해준다.
        cnt += a_b_sum.get(-(c+d), 0)
print(cnt)