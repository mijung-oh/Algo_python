left = { 1:4, 2:1, 3:2, 4:3 }
right = { 1:2, 2:3, 3:4, 4:1 }
direction = { 1: (0, 1), 2: (1,0), 3: (-1, 0), 4: (0,-1) }

def simul(idx, go, d, curX, curY):
    if idx == len(go): return

    if go[idx] == 'F' or go[idx] == 'B':
        
        simul(idx+1, go, d, curX+direction[d][0], curY+direction[d][1])
    elif go[idx] == 'L':
        simul(idx+1, go, left[d], curX, curY)
    elif go[idx] == 'R':
        simul(idx+1, go, right[d], curX, curY)
    
T = int(input())

for t in range(T):
    go = input()
    left_x = right_x = left_y = right_y = 0
    simul(0, go, 1, 0, 0)