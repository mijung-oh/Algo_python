N = int(input())

# map 초기화
map_s = [[0 for col in range(N)] for row in range(N)]

d = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽 아래 왼쪽 위

row = col = 0

while 1: 
    for i in range(4):
        map_s[row][col] = target
        target += 1
        
    