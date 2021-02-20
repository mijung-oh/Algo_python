N = int(input())

switch = [0]
switch += list(map(int, input().split()))

stu = int(input())

def change(x):
    if x == 0:
        return 1
    else:
        return 0

def man(num):
    for s in range(1, len(switch)):
        # num의 배수이면 스위치 상태를 바꿔줌
        if s % num == 0:
            switch[s] = change(switch[s])

def woman(num):
    i = 0
    switch[num] = change(switch[num])
    # 좌우대칭인 부분 찾기
    while num-i > 0 and num + i < len(switch):
        if switch[num-i] == switch[num+i]:
            switch[num - i] = change(switch[num-i])
            switch[num + i] = change(switch[num+i])
        else:
            break
        i += 1

for s in range(stu):
    gender, number = map(int,input().split())
    # 1이면 남자 2이면 여자
    if gender == 1:
        man(number)
    else:
        woman(number)
switch = switch[1:]

# 출력
for i in range(1, len(switch)+1):
    print(switch[i-1], end=' ')
    if i !=0 and i%20 ==0:
        print()
