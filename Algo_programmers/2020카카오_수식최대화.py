from itertools import combinations, permutations
import re

def solution(expression):
    answer = -1
    # expression에 나온 연산을 꺼낸 뒤
    orders = set()
    stack = []
    num = []
    for e in expression:
        if e in ['*', '-', '+']:
            stack.append(''.join(num))
            stack.append(e)
            num = []
            orders.add(e)
        else:
            num.append(e)
    stack.append(''.join(num))

    # 연산들의 우선순위를 정한다. => 조합생성
    orders_priority = list(permutations(orders, len(orders)))

    # stack을 활용하여 우선순위대로 연산을 수행한다.
    for order in orders_priority:
        right = stack[::]
        left = []
        for o in order:
            while right:
                cur = right.pop(0)
                if cur == o:
                    op1 = int(left.pop())
                    op2 = int(right[0])
                    right.pop(0)

                    # 연산하기
                    if o == '*': left.append(op1*op2)
                    elif o == '+': left.append(op1+op2)
                    elif o == '-': left.append(op1-op2)
                else:
                    left.append(cur)
            right = left[::]
            left = []
        
        # 최대값 선정
        if answer < abs(right[0]):
            answer = abs(right[0])
    return answer

solution("100-200*300-500+20")