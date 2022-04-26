N = int(input())
check = [0 for _ in range(10)] # 0-9 
cnt = 0
def dfs(cur_string, cur):
    global cnt
    if len(cur_string) == N:
        # 만약 0-9 숫자가 모두 check 됐으면
        if sum(check) == 10:
            cnt += 1
        return
    for i in [-1, 1]:
        if 0 <= cur + i < 10:
            check[cur+i] = 1
            dfs(cur_string + str(cur+i), cur+i)
            check[cur+i] = 0
    return

for i in range(1, 10):
    check[i] = 1
    dfs(str(i), i)
    check[i] = 0
print(cnt)
