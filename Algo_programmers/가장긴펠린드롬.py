def solution(s):
    answer = 0
    
    idx = 0
    length = 0
    # idx를 기준으로 길이 length만큼 앞뒤로 똑같은지 확인
    def check(loc, l):
        for i in range(1, l+1):
            if loc-i < 0 or loc+i >= len(s): 
                return False
            if s[loc-i] != s[loc+i]:
                return False
        return True
    
    while idx < len(s)-1:
        # 현재 최대 길이부터 length까지
        for l in range(answer+1, length+1):
            if check(idx, l):
                print("==", idx, l)
                answer = l
        idx += 1
        length += 1
            
    if answer:
        print(answer * 2 + 1)
        return answer * 2 + 1
    return 1

solution("AAAA")