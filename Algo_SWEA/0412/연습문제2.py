

# 문자열로 들어온 16진수 문자를
# 1. 2진수 비트로 바꾼다.
# 2. 7개씩 묶은 다음에
# 3. 10진수로 변경한다.
d = {
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
}
# 16진수로 변경
def strtobit(string):
    result = ''
    for i in string:
        for j in range(3, -1, -1):
            target = int(i) if i.isdecimal() else d[i]
            if target & 1<<j:
                result += '1'
            else:
                result += '0'
    return result


# 10진수로 변경
def binTodec(string):
    result = 0
    cnt = 0
    for i in range(len(string)-1, -1, -1):
        if int(string[i]):
            result += 1<<cnt
        cnt += 1
    return result

a = input()
bit = strtobit(a)
for i in range(0, len(bit), 7):
    print(binTodec(bit[i:i+7]))