from collections import deque
import sys
INF = sys.maxsize

st, en = map(int, input().split())

time = 0
loc = [INF] * (100001)
loc[st] = 0

q = deque()
q.append((st, 0))

while q:
    cur, time = q.popleft()
    if st < cur-1 <= 100000 and loc[cur-1] > time + 1:
        loc[cur-1] = time + 1
        q.append((cur-1, time+1))

    if st < cur+1 <= 100000 and loc[cur+1] > time + 1:
        loc[cur+1] = time + 1
        q.append((cur+1, time+1))

    if st < cur*2 <= 100000 and loc[cur*2] > time + 1:
        loc[cur*2] = time + 1
        q.append((cur*2, time+1))
# for i in range(5, 18):
#     print(i, end=" ")
# print()
# for i in range(5, 18):
#     print(loc[i], end=" ")
print(loc[en])