import math
def solution(arr):
    answer = 1

    # 최대공약수를 구한다.
    def f(array):
        result = 1
        for i in range(2, max(array)):
            check = True
            for j in array:
                if j % i:
                    check = False
                    break
            if check: 
                result = max(result, i)
        return result

    i = f(arr)
    if i == 1:
        for a in arr:
            answer *= a
        return answer

    while i != 1:
        aa = []
        # 최대공약수 곱해주고
        answer *= i
        for a in arr:
            aa.append(a // i)
            answer *= a // i
        # arr 초기화 해주고
        arr = aa[::]
        # 최대공약수 초기화
        i = f(arr)

    print(answer)
    return answer
solution([1,2,3])