# 포스트오더 식을 만들어서
# 리스트에 넣어준 뒤
# 계산해준다.

import sys
sys.stdin = open('사칙연산.txt', 'r')

def calc(number, op):
    while op:
        if len(number) == 1 and len(op) == 0:
            break
        current = op.pop(0)
        # 연산진행
        if current == '*':
            st = number.pop(0)
            en = number.pop(0)
            number.append(float(st) * float(en))
        elif current == '+':
            st = number.pop(0)
            en = number.pop(0)
            number.append(st + en)
        elif current == '/':
            st = number.pop(0)
            en = number.pop(0)
            number.append(st / en)
            # if st == 0 or en == 0:
            #     number.append(0)
            # else:
            #     number.append(st / en)
        elif current == '-':
            st = number.pop(0)
            en = number.pop(0)
            number.append(abs(st-en))
        print(number)



def tr(idx):
    global node
    if idx <= node:
        #왼쪽 오른쪽 중간
        tr(idx*2)
        tr(idx*2+1)
        if G[idx] == '*' or G[idx] == '+' or G[idx] == '/' or G[idx] == '-':
            op.append(G[idx])
        else:
            number.append(int(G[idx]))

for tc in range(1, 11):
    node = int(input())
    G = [0] * (node+1)

    # 숫자랑 연산자를 따로 넣어둠
    number = []
    op = []

    # 트리만들기
    for n in range(node):
        lst = input().split()
        G[int(lst[0])] = lst[1]

    tr(1)
    calc(number, op)
    result = int(number[0])
    print('#{} {}'.format(tc, result))