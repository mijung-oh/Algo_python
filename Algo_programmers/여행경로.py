def solution(tickets):
    answer = []
    s = ["ICN"]
    visited = [0] * len(tickets)

    def dfs(cur, visited, tickets, state):
        nonlocal answer
        
        if len(state) == len(tickets) + 1:
            answer = state
            return True 
            
        for idx, ticket in enumerate(tickets):
            if visited[idx]:
                continue
            if ticket[0] == cur:
                check = 0
                visited[idx] = 1
                state.append(ticket[1])

                if dfs(ticket[1], visited, tickets, state):
                    return True
                    
                visited[idx] = 0
                state.pop()

        return False
    tickets.sort()
    dfs("ICN", visited, tickets, s)
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
