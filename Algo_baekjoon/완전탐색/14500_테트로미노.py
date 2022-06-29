R, C = map(int, input().split())
BRD = [list(map(int, input().split())) for r in range(R)]
result = -1
shape = {
    1: []
}
def dfs(r, c, road):
    if len(road) == 4:
        sub = 0
        for i in range(len(road)):
            sub += BRD[road[i][0]][road[i][1]]
        result = max(result, sub)
        return
    
    # road 의 개수에 따라 선택할 수 있는 칸의 개수가 다르다.
    # 선택할 칸의 개수
    for i in range(4-len(road)):
        pass

