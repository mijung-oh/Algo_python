def solution(n, t, m, timetable):
    answer = ''

    # 시간을 분단위로 바꾼다.
    # 셔틀 출발 시간
    cur_bus = 9 * 60

    # timetable을 분단위로 바꾼다.
    new_timetable = []
    for time in timetable:
        hh, mm = int(time.split(":")[0]), int(time.split(":")[1])
        new_timetable.append(hh * 60 + mm)
    new_timetable.sort()

    # 버스 오는 횟수
    for i in range(1, n+1):
        cnt = 0
        for time in new_timetable:
            if cur_bus >= time:
                cnt += 1

        # 마지막 버스가 아닌 경우
        if i != n:
            # 버스 출발 시간보다 일찍 대기한 사람 수를 세고, m이하만큼 pop한다.
            if cnt > m:
                cnt = m
            while cnt:
                new_timetable.pop(0)
                cnt -= 1
        # 마지막 버스인 경우
        else:
            # 버스 출발 시간보다 대기한 수가 m 이상이면
            if cnt >= m:
                # m번째 사람보다 1분 늦게 간다
                answer = new_timetable[m-1]-1
                break
            else:
                answer = cur_bus
        # 버스시간 업데이트
        cur_bus += t

        
    ans_h = str(answer // 60)
    ans_m = str(answer % 60)
    if len(ans_h) == 1:
        ans_h = '0' + ans_h
    if len(ans_m) == 1:
        ans_m = '0' + ans_m
    answer = ans_h + ":" + ans_m
    print(answer)
    return answer

solution(2,1,2,["09:00", "09:00", "09:00", "09:00"])