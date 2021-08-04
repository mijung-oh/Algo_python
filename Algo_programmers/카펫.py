def solution(brown, yellow):
    answer = []
    sero = 1
    garo= yellow

    while sero <= garo and sero * garo ==  yellow:
        print(garo, sero)
        if (sero+2) * (garo+2) == brown + yellow:
            answer.append(garo+2)
            answer.append(sero+2)
            break
        sero += 1
        garo = yellow // sero
    return answer


print(solution(8,1))

