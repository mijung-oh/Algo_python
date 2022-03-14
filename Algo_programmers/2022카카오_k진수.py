# 소수판별
def isPrime(number):
    number = int(number)
    if number <= 1:
        return False
    for i in range(2, number//2):
        if number % i == 0:
            return False
    return True


# k진수로 변경
def change(number, k):
    remains = []
    while number:
        remains.append(number%k)
        number //= k
    return list(reversed(remains))

def solution(n, k):
    answer = 0
    # k 진수로 변경한다.
    number = change(n, k)

    # 0을 마주하기 전의 숫자를 골라낸 후, 그 숫자가 소수인지 판별한다.
    cur = []
    for idx, n in enumerate(number):
        if n == 0:
            if cur:
                cur_num = "".join(map(str, cur))
                if isPrime(cur_num):
                    answer += 1
                cur = []
        # 마지막 원소인 경우 0을 마주할 일이 없으므로 합쳐서 한번 더 같은 과정 진행
        elif idx == len(number)-1:
            cur.append(n)
            cur_num = "".join(map(str, cur))
            if isPrime(cur_num):
                answer += 1
        else:
            cur.append(n)
    print(answer)
    return answer

solution(524287,2)