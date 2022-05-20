from collections import deque

def solution(maps):
    answer = 0
    visited = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    visited[0][0] = 1
    q = deque()
    q.append((0,0))
    while q:
        cur_r, cur_c = q.popleft()
        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            new_r = cur_r + d[0]
            new_c = cur_c + d[1]
            if 0 <= new_r < len(maps) and 0 <= new_c < len(maps[0]) and maps[new_r][new_c]:
                if visited[new_r][new_c] == -1 or visited[new_r][new_c] > visited[cur_r][cur_c] + 1:
                    visited[new_r][new_c] = visited[cur_r][cur_c] + 1
                    q.append((new_r, new_c))
    return answer
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])