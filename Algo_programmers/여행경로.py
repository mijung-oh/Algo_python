def dfs(cur, visited, tickets, state, answer):
    check = 1
    for idx, ticket in enumerate(tickets):
        if visited[idx]:
            continue
        if ticket[0] == cur:
            check = 0
            visited[idx] = 1
            state.append(ticket[1])
            answer = dfs(ticket[1], visited, tickets, state, answer)
            visited[idx] = 0
            state.pop()

    # 다음 경로가 없을 경우
    if check:
        if answer == []:
            answer = state
            return answer
        else:
            print(answer, state)
            answer_string = ''.join(answer)
            state_string = ''.join(state)
            if answer_string > state_string:
                answer = state
            return answer

    print('마지막,', answer)
    return answer
    




def solution(tickets):
    answer = []
    s = ["ICN"]
    visited = [0] * len(tickets)
    answer = dfs("ICN", visited, tickets, s, [])
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
