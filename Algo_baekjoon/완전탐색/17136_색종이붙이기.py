import sys
BRD = [list(map(int, input().split())) for _ in range(10)]
maxCount = [[0 for _ in range(10)] for _ in range(10)]

'''
1. 각 칸을 돌면서 nxn 정사각형이 나오는지 확인한다.
2. 정사각형이 되는 경우의 수를 돈다.
'''
# paper[i] => ixi 크기 색종이 개수
paper = [5 for _ in range(6)]

def check(r,c):
    canSquare = []
    # 색종이 크기
    for l in range(1, 6):
        count = 0
        for rr in range(l):
            if r + rr < 10:
                count += sum(BRD[r + rr][c:c+l])
            else: break
        if count == l * l:
            canSquare.append(l)
    canSquare.sort(reverse=True)
    return canSquare

answer = sys.maxsize
def dfs(cnt):
    global answer
    if cnt >= answer:
        return
    
    if sum(paper) == 0:
        return

    # 만약 1이 없다면
    exist = False
    for r in range(10):
        for c in range(10):
            if BRD[r][c] == 1:
                exist = True
                break
        if exist:
            break
    
    if not exist:
        answer = min(answer, cnt)
        return

    for r in range(10):
        for c in range(10):
            if BRD[r][c] == 1:
                # print(r, c, check(r,c))
                for l in check(r,c):
                    # 색종이가 있다면
                    if paper[l]:
                        paper[l] -= 1
                        # 정사각형크기만큼 0으로 바꾸기
                        for i in range(r, r+l):
                            for j in range(c, c+l):
                                BRD[i][j] = 0
                        # print(r, c, l)
                        # for i in range(10):
                        #     print(*BRD[i])
                        dfs(cnt + 1)
                        paper[l] += 1
                        # 정사각형크기만큼 1로 바꾸기
                        for i in range(r, r+l):
                            for j in range(c, c+l):
                                BRD[i][j] = 1
                    
    return
dfs(0)
if answer != sys.maxsize:
    print(answer)
else:
    print(-1)
