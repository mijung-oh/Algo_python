def solution(s):
    answer = ''
    t = list(map(int, s.split()))
    t = sorted(t)
    answer += str(t[0])
    answer += " "
    answer += str(t[-1])
    return answer