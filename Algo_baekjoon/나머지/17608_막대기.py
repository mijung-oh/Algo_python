import sys
N = int(input())
lst = [int(sys.stdin.readline().strip()) for _ in range(N)]

# print(lst)
min_size = lst[-1]
cnt = 1
for i in range(len(lst)-2, -1, -1):
    if min_size < lst[i]:
        cnt += 1
        min_size = lst[i]

print(cnt)