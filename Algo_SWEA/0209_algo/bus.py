# T = int(input())

# for t in range(1, T+1):
#     k, n, m = map(int, input().split())
#     stop = list(map(int, input().split()))

#     # 초기화
#     cnt = 0
#     move = 0
#     start = 0

#     while 1:
#         start += 1
#         move += 1
#         if start == n:
#             break

#         if move == k:
#             if start in stop:
#                 cnt += 1
#                 move = 0
#             else:
#                 check = 0
#                 for s in range(start-1, start-k, -1):
#                     if s in stop:
#                         start = s
#                         cnt+=1
#                         move=0
#                         check = 1
#                         break
#                 if check == 0:
#                     cnt = 0
#                     break
#     print(f'#{t} {cnt}')

# inputs
T = int(input())

# exe
for t in range(1, T + 1):
# inputs
    K, N, M = map(int, input().split())
    Stops = list(map(int, input().split())) + [N]

# init
start = 0
cnt = -1

# exe
while True:
    if start == N:
        break
    for i in range(start + K, start, -1):
        if i in Stops:
            cnt += 1
            start = i
            break
    else:
        cnt = 0
        break
print(f'#{t} {cnt}')