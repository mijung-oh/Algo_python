T = int(input())

def f(brd):
    minCode = 1
    return


for t in range(T):
    N = int(input())
    BRD = []
    for n in range(N):
        BRD.append(list(map(int, input().split())))
    minCode = N*N
    f(BRD)
    print(minCode)

# 1
# 7    
# 0 0 1 0 0 0 0
# 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0
# 1 1 0 1 0 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 0 0