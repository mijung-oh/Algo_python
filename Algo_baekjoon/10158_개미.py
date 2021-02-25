w, h = map(int, input().split())
p,q = map(int, input().split())
time = int(input())

# 개미는 오른쪽 위 45도가 아닌 오른쪽 아리 45도가 디폴트로 움직임
# 디폴트: p+1, q+1

t = 0
pre = (p,q)
# 디폴트방향 (1,1)
d = (1,1)
while 1:
    t += 1

    # 만약 벽에 박으면 반사됨
    if p == w:
        # 전꺼랑 안같으면
        if p-1>=0 and q-1>=0 and (p-1, q-1) != pre:
            pre = (p, q)
            p -= 1
            q -= 1
            d = (-1, -1)
        else:
            pre = (p, q)
            p -= 1
            q += 1
            d = (-1, 1)
    elif q == h:
        # 전꺼랑 안같으면
        if p-1>=0 and q-1>=0 and (p-1, q-1) != pre:
            pre = (p, q)
            p -= 1
            q -= 1
            d = (-1, -1)
        else:
            pre = (p, q)
            p += 1
            q += 1
            d = (1,1)
    elif p == 0:
        # 전꺼랑 안같으면
        if p-1>=0 and q+1 < h and (p-1, q+1) != pre:
            pre = (p, q)
            p -= 1
            q += 1
            d = (-1, 1)
        else:
            pre = (p, q)
            p += 1
            q += 1
            d = (1,1)
    elif q == 0:
        # 전꺼랑 안같으면
        if p-1 >= 0 and q +1 < h and (p-1, q+1) != pre:
            pre = (p, q)
            p -= 1
            q += 1
            d = (-1,1)
        else:
            pre = (p, q)
            p += 1
            q += 1
            d = (1,1)
    else:
        # 시간초과인데,,, 반사되기 직전에 바로 점프해서 가야할거같은데..
        while 1:
            pre = (p,q)
            p += d[0]
            q += d[1]
            t += 1
            if p == w or q == h or p == 0 or q == 0:
                t -= 1
                break
    if t ==time:
        break
print(p,q)