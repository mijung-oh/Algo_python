## counting sort
import sys
input = sys.stdin.readline
N = int(input())

count = [0 for i in range(10001)]
for n in range(N):
    count[int(input())] += 1

for idx, cnt in enumerate(count):
    if cnt != 0:
        for c in range(cnt):
            print(idx)