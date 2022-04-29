def solution(s):
    answer = len(s)
    
    for i in range(2, len(s)//2+1):
        sub_result = []
        st = 0
        while 1:
            if st > len(s)-i: break
            # i 길이만큼 뽑는다.
            ss = s[st: st+i]
            print(i, ss)
            cnt = 0
            # st+i부터 해당 문자열을 가지고 있는지 확인한다.
            while 1:
                if ss == s[st: st+i]:
                    st += i
                    cnt += 1
                else:
                    print("==", ss, sub_result, st)
                    sub_result.append(s[st])
                    st += 1
                    break
            # 만약 반복 문자열이 있었다면
            if cnt:
                if cnt > 1:
                    sub_result.append(str(cnt))
                sub_result.append(ss)
            # 만약 st가 s 바깥을 가리키고 있다면 break
        print(sub_result)
        answer = min(answer, len(''.join(sub_result)))
            
            
    return answer
solution("aabbaccc")