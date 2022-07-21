from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    isVisit = []

    # 불량사용자에 포함되는지 확인
    def isBanned(sub_user_id):
        for i in range(len(sub_user_id)):
            if len(banned_id[i]) != len(sub_user_id[i]):
                return False
            
            for j in range(len(sub_user_id[i])):
                if banned_id[i][j] == "*":
                    continue
                if banned_id[i][j] != sub_user_id[i][j]:
                    return False
        return True
    
    for perm in permutations(user_id, len(banned_id)):
        if sorted(perm) in isVisit:
            continue
        if isBanned(perm):
            isVisit.append(sorted(perm))
            answer += 1

    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))