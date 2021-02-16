
def myAbs(value):
    if value > 0:
        return value
    else:
        return value*-1

#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ARR = [[9, 9, 9, 9, 9] * 5]

sumV = 0
for r in range(5):
    for c in range(5):
        for i in range(4):
            newR = r+dr[i]
            newC = c+dc[i]
            if newR >= 0 and newR < N and newC >=0 and newC < N:
                sumV += myAbs(ARR[r][c] - ARR[newR][newC])