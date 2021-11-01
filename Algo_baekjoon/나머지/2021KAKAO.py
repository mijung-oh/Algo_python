def solution(new_id):
    answer = ''
    id_list = []
    id_list.extend(new_id)

    # 대문자 -> 소문자
    for idx, id in enumerate(id_list):
        if 65 <= ord(id) <= 90:
            id_list[idx] = chr(ord(id)+32)

    # 소문자, 숫자, 빼기, 밑줄, 마침표 제외한 모든 문자 제거
    id_list_2 = id_list[:]
    print(id_list)
    for idx, id in enumerate(id_list_2):
        if 97 <= ord(id) <= 122 or id.isdecimal() or id == '-' or id == '_' or id == '.':
                continue
        id_list.remove(id)
    print(id_list)
    # 마침표가 2번 이상 연속되면 하나로 치환,
    count = 0
    id_list_2 = id_list[:] + ['A']
    print(id_list_2)
    for idx, id in enumerate(id_list_2):
        if id == '.' and count == 0:
            count += 1
        elif id == '.' and count !=0:
            count += 1
        elif id != '.' and count != 0:
            for i in range(1, count):
                id_list[idx-i] = 'A'
            count = 0
    id_list_2 = id_list[:]
    print(id_list)

    for i in id_list_2:
        if i == 'A':
            id_list.remove(i)
    print(id_list)

    # 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(id_list) >0 and id_list[0] == '.':
        id_list.remove(id_list[0])
    if len(id_list) >0 and id_list[-1] == '.':
            id_list.remove(id_list[-1])       

    # new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(id_list) == 0:
        id_list.append("a")
    
    # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(id_list) >= 16:
        id_list = id_list[:15]
        if id_list[-1] == '.':
            id_list.remove(id_list[-1])

    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(id_list) <= 2:
        last = id_list[-1]
        while len(id_list) != 3:
            id_list.append(last)

    id_str = ''.join(id_list)
    return id_str

print(solution('..........A..........'))