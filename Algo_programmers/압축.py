def solution(msg):
    # 1. 계속해서 문자열을 만든다.
    # 2. 만든 문자열이 dict에 있다면 idx만 1 추가해주고 pass
    # 3. dict에 없다면 마지막 문자 제외한 문자는 있는 것이므로 해당하는 idx 추가하고 pass
    answer = []
    Dict = {chr(64 + i) : i for i in range(1, 27)}
    
    idx = 0
    search = ""
    baseNumber = 27

    while idx < len(msg):
        # search 업데이트
        search += msg[idx]
        print(search)

        if search in Dict:
            idx += 1
        else:
            # Dict에 정보 추가
            Dict[search] = baseNumber
            baseNumber += 1

            answer.append(Dict[search[:-1]])
            # search 초기화
            search = ""
    # 마지막 원소
    answer.append(Dict[search])
    return answer
solution("TOBEORNOTTOBEORTOBEORNOT")