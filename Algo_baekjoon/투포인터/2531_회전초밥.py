# N: 벨트 위의 접시 수
# d: 초밥 가짓수
# k: 연속해서 먹는 접시 수
# c: 쿠폰 번호
# 연속 k개 접시 먹으면 할인가능 + 하나 무료로 제공 받음
# => 연속 k개를 뽑는데, 겹치는 것이 없도록 뽑는다...
# 쿠폰번호가 없는 k개 가 베스트
N, d, k, c = map(int, input().split())
bab = []
for n in range(N):
    bab.append(int(input()))
result = -1
for st in range(len(bab)):
    new_bab = set()
    kk = k
    idx = st
    while kk:
        new_bab.add(bab[idx])
        idx = (idx+1) % len(bab)
        kk -= 1
    new_bab.add(c)
    result = max(result, len(new_bab))
print(result)
# k개씩 묶음
# for st in range(len(bab)):
#     # sub = []
#     idx = st
#     kk = k
#     # c랑 같은 것의 개수 중 가장 작은거
#     min_c = 3001
#     # c 개수
#     cnt_c = 0
#     while kk:
#         if c == bab[idx]:
#             cnt_c += 1
#         # sub.append(bab[idx])
#         idx = (idx+1) % len(bab)
#         kk -= 1
#     min_c = min(min_c, cnt_c)
# print(k+1-min_c)
