T = int(input())

def isRun(lst):
    for i in range(len(lst)-3+1):
        if lst[i]>0 and lst[i+1]>0 and lst[i+2]>0:
            return True
    return False


for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    player_1 = [0] * 10
    player_2 = [0] * 10
    winner = 0
    for i in range(len(lst)):
        if i%2:
            player_2[lst[i]] += 1
            if player_2.count(3) == 1 or isRun(player_2):
                winner = 2
                break
        else:
            player_1[lst[i]] += 1
            if player_1.count(3) == 1 or isRun(player_1):
                winner = 1
                break
    print('#{} {}'.format(tc, winner))