import sys
N = int(input())

result = sys.maxsize

a = b = 0
while 1:
    if 5 * b > N:
        break
    
    if (N - 5 * b) % 3 == 0:
        a = (N-5*b) // 3
        if a + b < result:
            result = a + b
    b += 1
print(result if result != sys.maxsize else -1)