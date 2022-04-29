N = int(input())

def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True

for n in range(N):
    s = input().rstrip()
    if isPalindrome(s):
        print(0)
    elif isSimilPalindrome(s):
        print(1)
    else:
        print(2)