def solution(gems):
    N = len(gems)
    answer = [1, N]

    types = {}
    for g in gems:
        types[g] = 0
    
    l = r = 0
    while l < N and r < N:
        for i in range(l, r+1):
            types[gems[i]] = 1
        
        # 보석을 다 포함했는지 여부
        check = True
        for k in types.keys():
            if types[k] == 0:
                check = False
                break
        if check:
            # 현재 최소 길이보다 짧을 경우 answer 업데이트
            if answer[1] - answer[0] > r - l:
                answer = [l+1, r+1]
            l += 1
        
        # 보석이 다 포함되어있지 않다면
        else:
            r += 1
        
        # types 초기화
        for k in types.keys():
            types[k] = 0
    return answer      
        
def solution(gems):
    N = len(gems)
    # 보석 총 개수
    count = len(set(gems))

    answer = [1, N]

    types = {gems[0]: 1}
    
    l = r = 0
    while l < N and r < N:
        
        # 보석을 다 포함했을 경우
        if count == len(types):
            # 기존 l위치의 보석을 뺀다.
            if types[gems[l]] == 1:
                del types[gems[l]]
            else:
                types[gems[l]] -= 1
            
            # 현재 최소 길이보다 짧을 경우 answer 업데이트
            if answer[1] - answer[0] > r - l:
                answer = [l+1, r+1]
            l += 1
        
        # 보석이 다 포함되어있지 않다면
        else:
            r += 1
            if r >= N: break

            # 업데이트된 r위치의 보석을 포함시킨다.
            if gems[r] in types.keys():
                types[gems[r]] += 1
            else:
                types[gems[r]] = 1

    print(answer)
    return answer
        
        
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])