from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    ban_list=  []

    def check(user, ban):
        for i in range(len(ban)):
            # 길이 자체가 다르면 False
            if len(user[i]) != len(ban[i]):
                return False
            
            for j in range(len(ban[i])):
                if ban[i][j] == '*': continue
                if user[i][j] != ban[i][j]:
                    return False
        return True

    for perm in permutations(user_id, len(banned_id)):
        if sorted(perm) in ban_list:
            continue
        if check(perm, banned_id):
            ban_list.append(sorted(perm))
    
    print(ban_list)
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))