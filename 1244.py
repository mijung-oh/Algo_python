N = int(input())

switch = [0]
switch += list(input().split())

stu = int(input())


def man(num):
    for s in range(1, len(switch)):
        # num의 배수이면 스위치 상태를 바꿔줌
        if s % num == 0:
            switch[s] = '1' if switch[s] == '0' else '0'

def woman(num):
    print('==')
    i = 0
    # 좌우대칭으로 같은 값이 존재하면 1, 존재하지 않으면 0
    check = 0
    while 1:
        i += 1
        if num-i <= 0 or num +i >= len(switch):
            break
        if num - i > 0 and num + i < len(switch):
            if switch[num-i] == switch[num+i]:
                check = 1
                switch[num - i] = '1' if switch[s] == '0' else '0'
                switch[num + i] = '1' if switch[s] == '0' else '0'
    if check == 0:
        switch[num] = '1' if switch[num] == '0' else '0'

for s in range(stu):
    gender, number = input().split()
    if gender == '1':
        man(int(number))
    else:
        woman(int(number))

print(switch)