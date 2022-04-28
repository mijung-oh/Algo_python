from cProfile import label
import sys
input = sys.stdin.readline

N = int(input())
words = []
for i in range(N):
    s = input().split()[0]
    words.append((len(s), s))

# 중복 제거
words = list(set(words))
words.sort(key=lambda x : (x[0], x[1]))
for w in words:
    print(w[1])