def isPalindrome(x):
    if x == x[::-1]:
        return True
    return False

def solution(s):
    answer = 0
    # 끝점
    for i in range(1, len(s)):
        # 길이
        for j in range(i):
            if i-j < answer:
                break
            if isPalindrome(s[j:i+1]):
                answer = i-j
    return answer+1

solution("A")
