import sys, time
sys.stdin = open('input.txt', 'r')
start = time.time()
def f(cnt):
    global maxV
    if cnt == 0:
        if maxV < int(''.join(numbers)):
            maxV = int(''.join(numbers))
        return
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            key = ''.join(numbers)
            if chk.get((key, cnt-1),1):
                chk[(key, cnt-1)] = 0
                f(cnt-1)
            numbers[i], numbers[j] = numbers[j], numbers[i]
 
 
T = int(input())
 
for t in range(1,T+1):
    numbers, N = input().split()
    N = int(N)
    numbers = list(numbers)
    maxV = 0
    chk = {}
    f(N)
    print('#{} {}'.format(t,maxV))
print(start/60)