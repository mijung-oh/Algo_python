def check(y, x): # 대각선 확인하는 함수 설정
    for j in range(y): # y의 현재 위치까지 순환하면서
        if y - j == abs(x-diagonal[j]): # y의 거리차이와 x의 거리차이가 같다면 체스를 둘 수 없으므로
            return False # False값 return 해주기
    return True # 거리차이 같지 않다면 체스를 둘 수 있으므로 True값 return
 
def queen(y):
    global cnt, result
 
    if y == N:
        if cnt == N: # x_visited에 잘 채워넣어서 tmp == N 이 되었다면
            result += 1 # 경우의 수(result)를 +1 해주기
        return
 
    for x in range(N):
        if not visited[x] and check(y, x):
            visited[x] = 1
            cnt += 1
            diagonal[y] = x
            queen(y+1)
            visited[x] = 0
            cnt -= 1
            diagonal[y] = 0
 
 
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
 
    visited = [0] * N
    diagonal = [0] * N
 
    cnt = 0
    result = 0
 
    queen(0)
 
    print("#{} {}".format(testcase, result))