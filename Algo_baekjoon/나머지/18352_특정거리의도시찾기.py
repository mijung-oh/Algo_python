from collections import deque

N, M, K, X = map(int, input().split())
BRD = dict()
dist = [-1] * (N+1)

for m in range(M):
    st, en = map(int, input().split())
    if st in BRD.keys():
        BRD[st].append(en)
    else:
        BRD[st] = [en]
        
q = deque()
q.append(X)
dist[X] = 0
while q:
    node = q.popleft()
    # 연결된 도시 돌기
    if node in BRD.keys():
        for next_node in BRD[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + 1
                q.append(next_node)
            
result = []
for node, v in enumerate(dist):
    if v == K:
        result.append(node)

if result:
    for r in sorted(result):
        print(r)
else:
    print("-1")