C, R = map(int, input().split())

#C:열개수 R:행개수
# 6X7
number = int(input())
# 방향은 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[0 for x in range(C)] for y in range(R)]
count = 1

def isTrue(x,y):
    count = 1
    if number == 1:
        return (1,1)

    while 1:
        for i in range(4):
            while 1:
                if 0<= x+dx[i]< R and 0<= y+dy[i] < C and visited[x+dx[i]][y+dy[i]] == 0:
                    x = x+dx[i]
                    y = y+dy[i]
                    visited[x][y] = 1
                    count += 1
                else:
                    break
                if count == number:
                    return (y+1,x+1)
# 초기위치
x=y=0
visited[x][y] = 1
if number <= C*R:
    result = isTrue(x,y)
else:
    result = 0
print(result)

