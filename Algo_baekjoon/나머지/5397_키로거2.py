import sys

def keyLogger(key):
    pointer = 0
    left = []
    right = []
    result = ""
    for k in key:
        if k == "<":
            # 왼쪽 스택 값을 오른쪽 스택으로 넣는다.
            if left:
                right.append(left.pop())
        elif k == ">":
            if right:
                left.append(right.pop())
        elif k == "-":
            if left:
                left.pop()
        else:
            # 기본 문자일 경우 left에 값을 넣는다.
            left.append(k)
    
    # for i in left:
    #     result += i
    # for j in range(len(right)-1, -1, -1):
    #     result += right[j]

    while right:
        left.append(right.pop())
    return left


N = int(sys.stdin.readline().strip())

for n in range(N):
    result = keyLogger(sys.stdin.readline().strip())
    print(''.join(result))
