import sys
input = sys.stdin.readline
import heapq
###################### bfs + pq ################
M, N = map(int, input().split())
# M: 가로, N: 세로
BRD = []
for m in range(M):
    BRD.append(list(map(int, input().split())))

# r,c 까지 오는데 경로 수
count = [[0 for _ in range(N)] for _ in range(M)]
count[0][0] = 1
q = []
# 시작점 추가
heapq.heappush(q, (-BRD[0][0],0,0))
# 우선순위큐를 사용하는 이유는 하나의 노드를 가는데
# 예를 들어 20을 가는데 경로가 
# 32 -> 20 이 있고, 32 -> 30 -> 25 -> 20 이 있는데,
# 우선순위큐를 사용하지 않을 경우 20 -> 17 -> 15 -> 10을 두 번 거쳐서 업데이트를 시켜준다.
# 이것을 방지하기 위해서 큰 노드부터 방문하도록 하고 방문했던 노드이면 q에 넣지 않는다. (재방문 방지)
# 만약 오름차순일경우 32 -> 20 -> 17 -> 15를 업데이트 한 뒤 30 -> 25 -> 20때 20만 업데이트가 된다.
# 이는 마지막 노드인 10까지 영향을 주지 않기 때문에 내림차순으로 해야한다.
# 즉 큰 원소부터
# 이걸 어떻게 생각해 ㅎ

while q:
    now, r, c = heapq.heappop(q)
    # now = -now
    # 각 요소를 돌며 본인보다 작은 요소인 경우 q에 담는다.
    # 만약 count값이 0이 아니라면 +1을 해준다.
    for d in [(1,0), (0,1), (0,-1), (-1,0)]:
        nr = r + d[0]
        nc = c + d[1]
        # 현재보다 작은 값일 경우
        if 0 <= nr < M and 0 <= nc < N and BRD[r][c] > BRD[nr][nc]:
            # 만약 다음 노드의 값이 0이 아닐 경우, 이미 방문한 노드이기 때문에
            # 중복탐색을 방지하기 위해 값을 업데이트만 하고 q에는 넣지 않는다.
            if count[nr][nc] != 0:
                count[nr][nc] += count[r][c]
                continue

            count[nr][nc] += count[r][c]
            heapq.heappush(q, (-BRD[nr][nc], nr, nc))
for i in range(len(count)):
    print(*count[i])
print(count[M-1][N-1])

############### 답안 코드 (dfs + dp) ###################
# def calc(rst, table, m, n, p, q):
#     # 마지막 원소일 경우, 그 곳까지 가는 길은 1이므로
#     if p == m-1 and q == n-1:
#         rst[p][q] = 1
#         return
#     # 와봤던 길이라면
#     if rst[p][q] != 0: return
#     rst[p][q] = 0

#     for dp, dq in [(1,0), (0,1), (-1,0), (0,-1)]:
#         np = p + dp
#         nq = q + dq
#         if 0 <= np < m and 0 <= nq < n and table[p][q] > table[np][nq]:
#             calc(rst, table, m, n, np, nq)
#             rst[p][q] += rst[np][nq]

# def solve():
#     m, n = map(int, sys.stdin.readline().rstrip().split())
#     table=  []
#     for _ in range(m):
#         arr = list(map(int, sys.stdin.readline().rstrip().split()))
#         table.append(arr)
#     rst = [[0] * n for _ in range(m)]
#     calc(rst, table, m, n, 0, 0)
#     for i in range(len(rst)):
#         print(*rst[i])
#     print(rst[0][0])
# solve()
