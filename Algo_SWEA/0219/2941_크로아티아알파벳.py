cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
# 문자열 안에 찾는 문자열이 존재하는 경우 시작 인덱스를 반환함
def find(s, x):
    # x: 찾을 문자열
    x_len = len(x)
    for i in range(len(s)-x_len+1):
        if x == ''.join(s[i:i+x_len]):
            print(x)
            return i
    return -1


word = list(input())
for i in cro:
    count += 1
    # 문자열 길이 2일때
    if i+2 <= len(cro)

print(count)