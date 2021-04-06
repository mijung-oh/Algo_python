def operation(c, a, b):
    if c == '*':
        return a*b
    elif c == '/':
        return a / b
    elif c == '+':
        return a + b
    elif c == '-':
        return a-b


def tr(root):
    global result
    if len(TREE[root]) > 1:
        result = operation(TREE[root][0], tr(TREE[root][1]), tr(TREE[root][2]))
        return result
    else:
        return TREE[root][0]


import sys
sys.stdin = open('사칙연산.txt', 'r')

for tc in range(1, 11):
    node = int(input())
    # 1부터 n번 노드, idx가 부모노드번호
    TREE = [[] for _ in range(node+1)]
    for n in range(1, node+1):
        lst = input().split()
        if len(lst) == 4:
            TREE[n].append(lst[1])
            TREE[n].append(int(lst[2]))
            TREE[n].append(int(lst[3]))
        else:
            TREE[n].append(int(lst[1]))
    result = 0
    tr(1)
    print('#{} {}'.format(tc, int(result)))
print(TREE)
