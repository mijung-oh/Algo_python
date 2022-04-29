from collections import deque
import sys
input = sys.stdin.readline

def solution(n):
    w1, w2, w3 = input().split()
    i = 0
    q = deque([(0, 0)])
    visited = [[0] * (len(w2)+1) for i in range(len(w1)+1)]
    while q:
        print(q)
        for _ in range(len(q)):
            a, b = q.popleft()
            if a < len(w1) and not visited[a+1][b] and w1[a] == w3[i]:
                visited[a+1][b] = 1
                q.append((a+1, b))
            if b < len(w2) and not visited[a][b+1] and w2[b] == w3[i]:
                visited[a][b+1] = 1
                q.append((a, b+1))
        i += 1
    tf = 'yes' if i == len(w3)+1 else 'no'
    print('Data set {0}: {1}'.format(n, tf))

if __name__ == '__main__':
    for i in range(1, int(input())+1):
        solution(i)