N = int(input())
num_lst = list(map(int, input().split()))
cnt = 1 # 시작시 바로 카운트,
max_v = 0

if N == 1:
    max_v = 1

# 연속 되는 큰 수를 구할때
for i in range(1, N):
    if num_lst[i-1] <= num_lst[i]:
        # print('i, cnt', i, cnt)
        cnt += 1
    else: #다시 1로 초기화 시켜주기
        cnt = 1
    if max_v < cnt:
        max_v = cnt
cnt = 1
# 연속 되는 작은 수를 구할때
for i in range(1, N):
    if num_lst[i-1] >= num_lst[i]:
        # print('2번째 i, cnt: ', i, cnt)
        # print(cnt)
        cnt += 1
    else: #다시 1로 초기화시켜주기
        cnt = 1
    if max_v < cnt:
        max_v = cnt


print(max_v)