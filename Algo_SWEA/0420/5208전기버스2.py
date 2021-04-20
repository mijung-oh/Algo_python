T = int(input())

def back(bat, current_idx, count, visited):
    global min_count
    # print(bat, current_idx, count)
    if current_idx == len(battery)-1:
        if min_count > count:
            min_count = count
        # print(visited, min_count)
        return min_count
    
    for i in [True, False]:
        # 선택하는 경우
        # 배터리 교체
        if i:
            if current_idx + 1 < len(battery) and count + 1 < min_count:
                visited[current_idx+1] = 1
                back(battery[current_idx+1], current_idx+1, count+1, visited)
                visited[current_idx+1] = 0
        # 선택 안하는 경우
        # 배터리가 1씩 감소
        else:
            if bat-1 > 0 and current_idx + 1 < len(battery) and count<= min_count:
                back(bat-1, current_idx+1, count, visited)
    return min_count

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    bus_stop = lst[0]
    battery = lst[1:]
    min_count = 0xffff
    visited = [0]*(len(battery)+1)
    print('#{} {}'.format(tc, back(battery[0], 0, 0, visited)))