def countBinOne(x):
    cnt = 0
    while x:
        if x % 2 == 1:
            cnt += 1
        x //= 2
    return cnt

def solution(n):
    answer = 0
    cnt = countBinOne(n)
    while 1:
        n += 1
        cnt2 = countBinOne(n)
        if cnt == cnt2:
            answer = n
            break
    print(answer)

    return answer

solution(78)