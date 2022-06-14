def solution(name):
    answer = 0

    # 초기 문자열
    init = "A" * len(name)
    # 조이스틱 위치
    idx = 0


    while name != init:
        if name[idx] == init[idx]:
            # 만약 현재 name 값과 init 위치값이 같다면
            # 이동할 곳을 찾는다.
            next_idx = 0
            gap = 1
            while 1:
                if name[idx+gap] != 'A':
                    next_idx = (idx+gap) % len(name)
                    break
            
            continue
    return answer

solution("JEROEN")