def solution(lines):
    answer = 0
    times = {}
    for i in range(60*60*24):
        times[i] = 0
    
    for line in lines:
        day, time, work = line.split()
        work = float(work[:len(work)-1])
        # time을 초단위로 변경
        hour, minute, sec = time.split(":")
        end = float(sec)*1000
        st = float(sec) - work * 1000 + 1

    return answer