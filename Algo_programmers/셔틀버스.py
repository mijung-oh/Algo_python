def solution(n, t, m, timetable):
    answer = ''
    ans_h = 0
    ans_m = 0
    # 버스는 n번만 온다. 그러므로 n번이 끝나기 전에 타야 한다.
    # 버스는 t분 간격으로 오고, m명까지 탈 수 있다.
    # n번째 버스를 마지막으로 타야 가장 늦게 탄다.
    # 버스가 도착한 시간
    cur_h = 9
    cur_m = 0

    timetable.sort()
    
    for bus in range(1, n+1):
        # 현재 버스를 탈 수 있는 인원을 구한다.
        possible = []
        for time in timetable:
            h, mi = int(time.split(":")[0]), int(time.split(":")[1])
            if h < cur_h:
                possible.append(time)
            elif h == cur_h and mi <= cur_m:
                possible.append(time)
        possible.sort()

        # 대기열이 있는 경우
        if possible:
            # 마지막 버스가 아닐 경우 l명을 pop한다.
            if bus != n:
                l = 0
                if len(possible) > m:
                    l = m
                else:
                    l = len(possible)
                while l:
                    timetable.pop(0)
                    l -= 1

            elif bus == n:
                print(possible, timetable)
                # 마지막 버스 인원이 더 많을 경우
                if len(possible) >= m:
                    # 가장 늦게 온 사람보다 1분 늦게 온다.
                    if int(possible[-1].split(":")[1])-1 < 0:
                        ans_h = int(possible[-1].split(":")[0])-1
                        ans_m = 59
                    else:
                        ans_h = int(possible[-1].split(":")[0])
                        ans_m = int(possible[-1].split(":")[1])-1
                        print("!!")
                    break
                else:
                    ans_h = cur_h
                    ans_m = cur_m

        # 현재 시간 업데이트
        tt = cur_m + t
        cur_h += tt // 60
        cur_m += tt % 60
        print("다음버스: ", cur_h, cur_m)

    print(ans_h, ans_m)
    return answer

solution(1,1,1,["23:59"])