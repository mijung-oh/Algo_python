import sys
s = sys.stdin.readline()
M, N = map(int, s.split())

def is_Prime(number):
    for num in range(2, number//2+1):
        if number % num == 0:
            return False

    return True

for i in range(M, N+1):
    if is_Prime(i):
        print(i)