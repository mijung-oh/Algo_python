result2 = []

def dfs(user_id, banned_id, cur, visited, state):
    if cur == len(banned_id):
        print(state)
        return 

    for user in range(len(user_id)):
        # usr와 ban이 같을 경우 dfs 재귀
        if visited[user]: continue

        if len(user_id[user]) == len(banned_id[cur]):
            check = True
            for k in range(len(user_id[user])):
                if banned_id[cur][k] != '*' and user_id[user][k] != banned_id[cur][k]:
                    check = False
                    break

            if check:
                visited[user] = 1
                state.append(user_id[user])
                dfs(user_id, banned_id, cur + 1, visited, state)
                visited[user] = 0
                state.pop()
    return

def solution(user_id, banned_id):
    global result2

    visited = [0] * len(user_id)
    banned_id = list(set(banned_id))
    state = []
    dfs(user_id, banned_id, 0, visited, state)
    print(result2)
    return result2

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))