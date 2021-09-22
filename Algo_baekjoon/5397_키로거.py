import sys

def keyLogger(key):
    pointer = 0
    result = ""
    for k in key:
        # stack에 값이 있으면서 왼쪽으로 포인터를 이동하는 경우
        if result and k == "<":
            if pointer <= 0:
                continue
            pointer -= 1
        elif result and k == ">":
            if pointer >= len(result):
                continue
            pointer += 1
        elif len(result) == 0 and (k == "<" or k == ">"):
            continue
        elif k == "-":
            result = result[:pointer-1]
            pointer -= 1
        elif k != "<" and k != ">":
            # pointer인 부분에 result 값이 있으면 앞뒤로 잘라서 해당 값을 넣는다.
            if pointer < len(result):
                left = result[:pointer]
                right = result[pointer:]
                result = left + k + right
                pointer += 1
            else:
                result += k
                pointer += 1
    return result


N = int(sys.stdin.readline().strip())

for n in range(N):
    print(keyLogger(sys.stdin.readline().strip()))
