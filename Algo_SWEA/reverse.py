string = '오미정'

def reverse(s):
    s_lst = list(s)
    l = len(s_lst)
    result = ''
    for i in range(l-1, -1, -1):
        result += s_lst[i]

    return result

print(reverse(string))