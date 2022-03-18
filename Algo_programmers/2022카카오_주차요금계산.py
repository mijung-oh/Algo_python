import math
def solution(fees, records):
    answer = []
    timesByCar = {}
    for record in records:
        time, car, d = record.split(" ")
        # 1. 차별로 시간을 저장한다.
        if car in timesByCar:
            timesByCar[car].append(time)
        else:
            timesByCar[car] = []
            timesByCar[car].append(time)
        
    # 차량번호가 작은 순으로 timesByCar를 정렬한다.
    timesByCar = dict(sorted(timesByCar.items()))

    # 시간 차이를 분단위로 계산한다.
    for key in timesByCar.keys():
        totalTime = 0

        for t in range(0, len(timesByCar[key]), 2):
            inTime = timesByCar[key][t]
            outTime = ""
            # 출차시간이 없는 경우 23:59로 계산
            if t+1 == len(timesByCar[key]):
                outTime = "23:59"
            else:
                outTime = timesByCar[key][t+1]
            
            # 분단위로 시간 계산
            if int(inTime[3:]) < int(outTime[3:]):
                totalTime += 60 * (int(outTime[:2]) - int(inTime[:2])) + (int(outTime[3:]) - int(inTime[3:]))
            else:
                totalTime += 60 * (int(outTime[:2]) - int(inTime[:2]) - 1) + (60 - int(inTime[3:]) + int(outTime[3:]))
        
        # 분단위 시간으로 요금 계산
        # fee: 기본시간 / 기본요금 / 단위시간 / 단위시간 당 요금
        if totalTime <= fees[0]:
            answer.append(fees[1])
        else:
            totalFee = fees[1] + math.ceil((totalTime-fees[0]) / fees[2]) * fees[3]
            answer.append(totalFee)

    # 기본시간 이상일경우 단위시간도 계산한다.
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	)