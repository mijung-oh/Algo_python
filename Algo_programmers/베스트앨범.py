def solution(genres, plays):
    answer = []
    genres_cnt = []
    # 장르 선택
    for idx, genre in enumerate(genres):
        check = 1
        for G in genres_cnt:
            if G[1] == genre:
                check = 0
                G[0] += plays[idx]
                break
        if check:
            genres_cnt.append([plays[idx], genre])

    genres_cnt.sort(key=lambda x: -x[0])

    # 재생 횟수가 많은 노래 선택
    for genre in genres_cnt:
        genres_cnt2 = []
        for idx, value in enumerate(genres):
            if value == genre[1]:
                genres_cnt2.append([plays[idx], idx, genre[1]])
        # 재생 횟구가 같을 경우 index가 낮은 노래 선택
        genres_cnt2.sort(key=lambda x : (-x[0], x[1]))
        print(genres_cnt2)
        # 각 장르별로 2개씩 선택
        if len(genres_cnt2) >= 2:
            answer.append(genres_cnt2[0][1])
            answer.append(genres_cnt2[1][1])        
        elif len(genres_cnt2) == 1:
            answer.append(genres_cnt2[0][1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))