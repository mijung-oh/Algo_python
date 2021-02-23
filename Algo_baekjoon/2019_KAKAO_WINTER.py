def solution(s):
    answer = []
    li = []
    sub_li = []
    flag = 0
    number = ''
    for idx, i in enumerate(s):
        # 처음과 끝이면 일단 패스
        if idx == 0  or idx == len(s)-1:
            continue
        
        if i == '{':
            flag = 1
            continue
        elif i.isdecimal() and flag:
            print(i)
            number += i
            print('==',number)
        elif i == ',':
            if number != '':
                sub_li.append(int(number))
                number = ''
            continue
        elif i == '}':
            if number != '':
                sub_li.append(int(number))
                number = ''
            li.append(sub_li)
            sub_li = []
            flag = 0
    print(li)
        
    for i in li:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))