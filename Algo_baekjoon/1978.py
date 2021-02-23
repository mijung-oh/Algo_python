import sys
T = int(sys.stdin.readline())

def is_Prime(number):
    if number == 1:
        return False
        
    for num in range(2, number//2+1):
        if number % num == 0:
            return False

    return True

result = 0
isPrime = list(map(int, sys.stdin.readline().split()))

for i in isPrime:
    if is_Prime(i):
        result += 1


print(result)