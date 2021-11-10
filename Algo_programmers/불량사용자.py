def solution(user_id, banned_id):
    answer = 0
    visited = [0] * len(user_id)
    banned_id = list(set(banned_id))

    for i in range(len(banned_id)):
        length = len(banned_id[i])

        for j in range(len(user_id)):
            if not visited[j] and length == len(user_id[j]):
                # 별 빼고 문자가 다 같은지 확인
                check = True

                for k in range(length):
                    if banned_id[i][k] != '*' and user_id[j][k] != banned_id[i][k]:
                        check = False
                        break
                
                if check:
                    # 겹치는 문자일 경우 visited 체크 후 다음 제재 아이디로 
                    print(user_id[j])
                    visited[j] = 1
                    break

    for i in range(len(visited)):
        if visited[i]:
            answer += 1
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))