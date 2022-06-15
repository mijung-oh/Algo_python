'''
1. 같은 칸이면 그냥 간다.
2. 다음 칸이 다른 칸일 경우, 
2-1) 갭이 2 이상이면 불가능
2-2) 갭이 1 이면서 경사로 설치 가능한지 확인하기. - 경사로 배열을 만들어서 체크한다.

'''
N, L = map(int, input().split())
BRD = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# 가로 길
for r in range(N):
    # 경사로 체크
    visited = [0] * N
    # 다음 칸을 갈 수 있는지 확인한다.
    can_go = True
    for c in range(N-1):
        # 만약 다음 칸이 1 크면
        if BRD[r][c+1] == BRD[r][c] + 1:
            # 현재칸에서 L크기만큼 경사로를 놓을 수 있다면
            for cc in range(c-L+1, c+1):
                if BRD[r][cc] == BRD[r][c] and not visited[cc]:
                    # 경사로 놓기
                    visited[cc] = 1
                else:
                    can_go = False
                    break
                
        # 만약 다음 칸이 1 작으면
        elif BRD[r][c+1] == BRD[r][c] - 1:
            for cc in range(c+1, c+1+L):
                if cc < N and BRD[r][cc] == BRD[r][c+1] and not visited[cc]:
                    # 경사로 놓기
                    visited[cc] = 1
                else:
                    can_go = False
                    break
        elif BRD[r][c+1] == BRD[r][c]:
            continue
        else:
            can_go = False
            break
        if not can_go: break
    if can_go:
        answer += 1

# 세로 길
for c in range(N):
    # 경사로 체크
    visited = [0] * N
    # 다음 칸을 갈 수 있는지 확인한다.
    can_go = True
    for r in range(N-1):
        # 만약 다음 칸이 1 크면
        if BRD[r+1][c] == BRD[r][c] + 1:
            # 현재칸에서 L크기만큼 경사로를 놓을 수 있다면
            for rr in range(r-L+1, r+1):
                if BRD[rr][c] == BRD[r][c] and not visited[rr]:
                    # 경사로 놓기
                    visited[rr] = 1
                else:
                    can_go = False
                    break
                
        # 만약 다음 칸이 1 작으면
        elif BRD[r+1][c] == BRD[r][c] - 1:
            for rr in range(r+1, r+1+L):
                if rr < N and BRD[rr][c] == BRD[r+1][c] and not visited[rr]:
                    # 경사로 놓기
                    visited[rr] = 1
                else:
                    can_go = False
                    break
        elif BRD[r+1][c] == BRD[r][c]:
            continue
        else:
            can_go = False
            break
        if not can_go: break
    if can_go:
        answer += 1

print(answer)