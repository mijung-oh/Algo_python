T = int(input())

def binTodec(string):
    result = ''
    value = str(float(string) * 2)
    while 1:
        if len(result) >12: return False
        if float(value) == 0: break
        result += value[0]
        value = '0' + value[1:]
        value = str(float(value) * 2)
        print(value)

    return result

for tc in range(1, T+1):
    binary = input()
    r = binTodec(binary)
    if r: print('#{} {}'.format(tc,r))
    else: print('#{} overflow'.format(tc))

