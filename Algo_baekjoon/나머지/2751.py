import sys

N = int(sys.stdin.readline())
n_list = []
for i in range(N):
    number = int(sys.stdin.readline())
    n_list.append(number)

for n in sorted(n_list):
    print(n)