def solution(s):
    answer = []
    s_list = s.split(" ")
    for word in s_list:
        new_word = []
        if word == "":
            new_word.append(" ")
            answer.append("")
            continue
        new_word.append(word[0].upper())
        for i in range(1, len(word)):
            new_word.append(word[i].lower())
        answer.append(''.join(new_word))
    return ' '.join(answer)