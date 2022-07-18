def solution(stones, k):
    answer = 0
    # 다음 위치를 알려주는 함수
    def nextLoc(cur):
        cnt = 0
        for loc in range(cur+1, len(stones)):
            cnt += 1
            # print(cur, loc, k, stones[loc])
            # 이동횟수가 k보다 크다면 X
            if cnt > k:
                return False
            if stones[loc]:
                return cnt
        return True            

    check = True
    while check:
        cur_loc = -1
        answer += 1
        while cur_loc < len(stones)-1:
            # 다음으로 갈 수 있는 위치를 받는다.
            nx = nextLoc(cur_loc)
            print(nx, cur_loc, len(stones), stones)
            # nx가 있다면 -> 다음으로 갈 수 있다는 것
            if nx:
                cur_loc += nx
                # 징검다리 업데이트
                stones[cur_loc] -= 1
            else:
                print("??", cur_loc)
                check = False
                answer -= 1
                break
        
    print(answer)
    return answer
solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)