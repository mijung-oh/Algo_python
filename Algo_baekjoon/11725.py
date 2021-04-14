import sys
input = sys.stdin.readline

N = int(input())

G1 = [[] for _ in range(N+1)]
G2 = [[] for _ in range(N+1)]

R = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(N-1):
    P, C = map(int, input().split())
    G1[P].append(C)
    G2[C].append(P)


def isParent(x):
    visited[x] = 1
    if len(G1[x]):
        for target in G1[x]:
            if visited[target] == 0:
                R[x].append(target)
            if G1[target] and visited[target] != 1:
                isParent(target)
    if len(G2[x]):
        for target in G2[x]:
            if visited[target] == 0:
                R[x].append(target)
            if G2[target] and visited[target] != 1:
                isParent(target)

    return
isParent(1)
for i in range(2, N+1):
    for idx, r in enumerate(R):
        if i in r:
            print(idx)
            break
   