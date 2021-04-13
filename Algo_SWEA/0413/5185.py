d = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
}
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

T = int(input())
for tc in range(1, T+1):
    N, s = input().split()
    print('#{} {}'.format(tc, strtobit(s)))