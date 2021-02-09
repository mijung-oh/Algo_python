def solution(s):
    # 대문자로 치환
    new_s = []
    check = 0 # 전에 문자가 '.'인지 아닌지?
    for i in s:
        print(i, new_s)
        if 65 <= ord(i) <= 90: #소문자인 경우
            new_s.append(chr(ord(i)+32))
            if check == 1:
                check = 0
        elif 97 <= ord(i) <= 122 or i.isdecimal() or i == '-' or i == '_':
                new_s.append(i)
                if check == 1:
                    check = 0
        elif i == '.':
            if check == 0:
                new_s.append(i)
                check = 1
            else:
                continue
        elif len(new_s) and new_s[0] == '.':
            new_s.remove(new_s[0])
        elif len(new_s) and new_s[-1] == '.':
            new_s.remove(new_s[-1]) 
        elif len(new_s) == 0:
            new_s.append('a')
        elif len(new_s) >= 16:
            new_s = new_s[:15]
            if new_s[-1] == '.':
                new_s.remove(new_s[-1])
        elif len(new_s) <= 2:
            last = new_s[-1]
            while len(new_s) != 3:
                new_s.append(last)

    return ''.join(new_s)
    
print(solution("z-+.^."))