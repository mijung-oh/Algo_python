import sys
sys.stdin = open('거스름돈.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    money = int(input())

    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8
    
    while money >= 10:
        for idx, m in enumerate(moneys):
            if money >= m:
                money -= m
                cnt[idx] += 1
                break
    print('#{}'.format(tc))
    print(*cnt)
