def solution(s):
    answer = len(s)
    
    # 압축할 문자열 길이
    for step in range(1, len(s)-1):
        sub_string = []
        prev = s[:step]
        cnt = 1
        for j in range(step, len(s), step):
            if s[j:j+step] == prev:
                cnt += 1
            else:
                if cnt > 1:
                    sub_string.append(str(cnt))
                sub_string.append(prev)
                cnt = 1
                prev = s[j:j+step]
        # 마지막 추가
        if cnt > 1:
            sub_string.append(str(cnt))
        sub_string.append(prev)

        answer = min(answer, len(''.join(sub_string)))
        print(step, sub_string)
    print(answer)
            
    return answer
solution("aababab")