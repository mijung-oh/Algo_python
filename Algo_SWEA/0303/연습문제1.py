q = []
chu = 20

human = 1
q.append(human)
while 1:
    # 마이쮸를 자기 숫자 만큼 받는다.
    # 총 마이쭈의 개수를 줄인다.
    order = q.pop(0)
    chu -= order
    q.append(order)
    # 마이쮸 받은 사람은 뒤로 다시 가서 줄을 선다.
    # 새로운 사람이 들어온다.

