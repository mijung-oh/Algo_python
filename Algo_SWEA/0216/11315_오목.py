T = int(input())

def isCross(lst):
    # 정방향 a 반대방향 b
    cross_a = 0
    cross_b = 0
    l = len(lst)
    for i in range(l):
        for j in range(l):
            if i == j and lst[i][j] == 'o':
                cross_a += 1
            elif i+j == l-1 and lst[i][j] == 'o':
                print(i, j)
                cross_b += 1
    if cross_a == l or cross_b == l:
        return True
    return False

def isRow(lst):
    l = len(lst)
    for i in range(l):
        if lst[i].count('o') == l:
            return True
    return False

# def isCol(lst):
#     l = len(lst)
#     t=[]
#     for i in range(l):
#         t.append([k[i] for k in a])
#     for i in range(l):
#         if t[i].count('o') == l:
#             return True
#     return False

for t in range(1, T+1):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(input().split()))
    
    if isCross(lst) or isCol(lst) or isRow(lst):
        print(f'#{t} Yes')
    else: 
        print(f'#{t} No')
