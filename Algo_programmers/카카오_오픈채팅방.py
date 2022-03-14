from collections import UserDict


def solution(recode):
    answer = []
    sub_answer = []
    # map으로 유저아이디와 이름을 설정한다.
    users = {}
    for r in recode:
        # 공백으로 분리한다.
        orders = list(r.split(" "))
        if len(orders) == 3:
            order, user_id, nickname = orders[0], orders[1], orders[2]
        else:
            order, user_id = orders[0], orders[1]

        if order == "Enter":
            users[user_id] = nickname
            sub_answer.append((user_id, "in"))
        elif order == "Leave":
            sub_answer.append((user_id, "out"))
        elif order == "Change":
            users[user_id] = nickname
    
    # subanwer을 answer로 바꾼다.
    for s in sub_answer:
        nick = users[s[0]]
        if s[1] == "in":
            answer.append(nick + "님이 들어왔습니다.")
        elif s[1] == "out":
            answer.append(nick + "님이 나갔습니다.")
    print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])