king, rock, N = input().split()
king_c = ord(king[0])
king_r = int(king[1])
rock_c = ord(rock[0])
rock_r = int(rock[1])

# A:65, Z: 90
# 1 <= r <= 8
# 65 <= c <= 90

for n in range(int(N)):
    move = input()
    if move == 'R':
        king_c += 1
        # 킹이 체스판 밖으로 나갈 경우
        if not (1 <= king_r <= 8 and 65 <= king_c <= 72):
            king_c -= 1
            continue

        # 돌의 위치와 같다면
        if rock_c == king_c and rock_r == king_r:
            rock_c += 1

            # 돌이 체스판 밖으로 나갈 경우
            if not (1 <= rock_r <= 8 and 65 <= rock_c <= 72):
                rock_c -= 1
                king_c -= 1
        
        

    elif move == 'L':
        king_c -= 1
        if not (1 <= king_r <= 8 and 65 <= king_c <= 72):
            king_c += 1
            continue

        if rock_c == king_c and rock_r == king_r:
            rock_c -= 1
            if not (1 <= rock_r <= 8 and 65 <= rock_c <= 72):
                rock_c += 1
                king_c += 1
       

    elif move == 'B':
        king_r -= 1
        if not (1 <= king_r <= 8 and 65 <= king_c <= 72):
            king_r += 1
            continue

        if rock_c == king_c and rock_r == king_r:
            rock_r -= 1
            if not (1 <= rock_r <= 8 and 65 <= rock_c <= 72):
                rock_r += 1
                king_r += 1


    elif move == 'T':
        king_r += 1
        if not (1 <= king_r <= 8 and 65 <= king_c <= 72):
            king_r -= 1
            continue

        if rock_c == king_c and rock_r == king_r:
            rock_r += 1
            if not (1 <= rock_r <= 8 and 65 <= rock_c <= 72):
                rock_r -= 1
                king_r -= 1
        

    elif move == 'RT':
        king_r += 1
        king_c += 1
        if not (1 <= king_r <= 8 and 65 <= king_c <= 72):
            king_c -= 1
            king_r -= 1
            continue

        if rock_c == king_c and rock_r == king_r:
            rock_r += 1
            rock_c += 1
            if not (1 <= rock_r <= 8 and 65 <= rock_c <= 72):
                rock_c -= 1
                rock_r -= 1
                king_c -= 1
                king_r -= 1
        

    elif move == 'LT':
        king_r += 1
        king_c -= 1
        if not (1 <= king_r <= 8 and 65 <= king_c <= 72):
            king_c += 1
            king_r -= 1
            continue

        if rock_c == king_c and rock_r == king_r:
            rock_r += 1
            rock_c -= 1
            if not (1 <= rock_r <= 8 and 65 <= rock_c <= 72):
                rock_r -= 1
                rock_c += 1
                king_c += 1
                king_r -= 1
        
        

    elif move == 'RB':
        king_r -= 1
        king_c += 1
        if not (1 <= king_r <= 8 and 65 <= king_c <= 72):
            king_c -= 1
            king_r += 1
            continue

        if rock_c == king_c and rock_r == king_r:
            rock_r -= 1
            rock_c += 1
            if not (1 <= rock_r <= 8 and 65 <= rock_c <= 72):
                rock_c -= 1
                rock_r += 1
                king_c -= 1
                king_r += 1
        
       
    elif move == 'LB':
        king_r -= 1
        king_c -= 1
        if not (1 <= king_r <= 8 and 65 <= king_c <= 72):
            king_c += 1
            king_r += 1
            continue

        if rock_c == king_c and rock_r == king_r:
            rock_r -= 1
            rock_c -= 1
            if not (1 <= rock_r <= 8 and 65 <= rock_c <= 72):
                rock_r += 1
                rock_c += 1
                king_c += 1
                king_r += 1
        
        
    

print(chr(king_c) + str(king_r))
print(chr(rock_c) + str(rock_r))
