# 1. 문자열 뒤에 A 추가
# 2. 문자열 뒤집고 뒤에 B 추가

S = list(map(str, input()))
T = list(map(str, input()))

# 정방향 => 시간초과
# def change(s):
#     global result
#     if len(s) < len(T):
#         if change(s+'A'):
#             return True
#         ss = s[::-1]
#         if change(ss + 'B'):
#             return True
#     elif len(s) == len(T) and s == T:
#         # print('결과:',s)
#         return True
#     return False

# 역방향 T -> S
def change(t):
    if t == S:
        return True
    if len(t) >= len(S):
        if t[-1] == 'A':
            if change(t[:len(t)-1]):
                return True
        elif t[-1] == 'B':
            t = t[:len(t)-1]
            t = t[::-1]
            if change(t):
                return True
    return False

print(int(change(T)))

print(S, T)
구글링.... 후 ㅠㅠ..
while len(S) != len(T):
    # print(T)
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

print(1 if S == T else 0)

