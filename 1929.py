import sys
s = sys.stdin.readline()
M, N = map(int, s.split())

T = int(N**0.5)

check_list = [True]*(N+1)
# 0과 1은 소수가 아님
check_list[0] = False
check_list[1] = False

for i in range(2, T+1): # 2 3 4
    if check_list[i] == True:
        for j in range(i+i, N+1, i): # 배수들에 다 False 넣기
            check_list[j]=False
for idx, c in enumerate(check_list):
    if M <= idx <= N and c == True:
        print(idx)



