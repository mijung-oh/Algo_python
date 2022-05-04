from itertools import product

def solution(numbers):
    answer = set()
    numbers = list(numbers)
    visited = [0] * len(numbers)
    
    # 소수 확인
    def isPrime(x):
        if x <= 1: return False
        for i in range(2, x):
            if i > x ** 0.5: return True
            if x % i == 0: return False
        return True
    print(isPrime(121))
    # 문자열 만들기
    def bf(cur, l):
        if len(cur) == l:
            if isPrime(int(cur)):
                answer.add(int(cur))
                return True
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = 1
                bf(cur + str(numbers[i]), l)
                visited[i] = 0
                
    # 만들 숫자 길이
    for l in range(1, len(numbers)+1):
        # 시작 숫자
        for i in range(len(numbers)):
            visited[i] = 1
            bf(str(numbers[i]), l)
            visited[i] = 0
            
            
    print(answer)
    return answer
solution("011")