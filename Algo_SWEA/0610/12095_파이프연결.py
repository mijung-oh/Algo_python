# 1-4,5
# 2-5,6
# 3-4,5,1
# 4-5,6,2
# 5-2,3
# 6-1,4,5

T = int(input())

def dfs(cur_pipe):
    # 해당 칸의 파이프를 90도 간격으로 바꿔본 뒤
    for d in range(4):
        change_pipe = cur_pipe + d if cur_pipe + d < 7 else cur_pipe + d - 4
        

    # dfs 재귀호출을 실행한다.
    # 연결할 수 있는 번호가 없다면 return

for tc in range(1, T+1):
    N = int(input())
    BRD = []
    for n in range(N):
        BRD.append(list(map(int, input().split())))

    dfs()