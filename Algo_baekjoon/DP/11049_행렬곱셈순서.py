import sys
from xml.dom import minicompat
input = sys.stdin.readline

N = int(input())
result = 0
matrix = []
for n in range(N):
    r, c = map(int, input().split())
    matrix.append((r,c))

while len(matrix) > 1:
    min_r = 999999
    min_idx = 0
    for i in range(len(matrix)-1):
        r, c, rr = matrix[i][0], matrix[i][1], matrix[i+1][1]
        if r * c * rr < min_r:
            min_idx = i
            min_r = r * c * rr
    result += min_r
    matrix2 = []
    for i in range(len(matrix)):
        if i == min_idx:
            matrix2.append((matrix[i][0], matrix[i+1][1]))
            continue
        if i == min_idx + 1:
            continue
        matrix2.append(matrix[i])
    matrix = matrix2
print(result)

    
