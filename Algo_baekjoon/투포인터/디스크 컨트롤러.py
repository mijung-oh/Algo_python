import heapq

def solution(jobs):
    answer = 0
    l = len(jobs)
    cur_time = 0
    heap = []
    cnt = 0

    # 작업 요청 순으로 정렬
    jobs.sort(key=lambda x: x[0])
    for job in jobs:
        heapq.heappush(heap, [job[1], job[0]])

    h = []
    # 현재 시간보다 작은 것 중 가장 작업소요시간이 작은 일을 처리한다.
    while cnt < l:
        # 현재 시간보다 작은 시간의 값을 heap에 넣는다.
        for job in jobs:
            if job[0] != -1 and job[0] <= cur_time:
                heapq.heappush(h, [job[1], job[0]])
                job[0] = -1
        if len(h) == 0:
            cur_time += 1
            continue
        
        print("h: ", h)

        time, st = heapq.heappop(h)
        cnt += 1
        cur_time += time
        print(st, time, cur_time)
        answer += abs(cur_time - st)
            
    print(answer // l)
    return answer // l

solution([[0, 3], [4, 4], [5, 3], [4, 1]])