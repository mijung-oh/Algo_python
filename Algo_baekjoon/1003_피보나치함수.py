T = int(input())

def fibo(n):
    if n > 1 and zero[n-1] == 0 and one[n-1] == 0:
        fibo(n-1)
    
    if n == 0:
        zero[n] = 1
        one[n] = 0
    elif n == 1:
        zero[n-1] = 1
        one[n-1] =0
        zero[n] = 0
        one[n] = 1
    else:
        zero[n] = zero[n-2] + zero[n-1]
        one[n] = one[n-2] + one[n-1]


for tc in range(T):
    n = int(input())
    zero = [0] * (n+1)
    one = [0] * (n+1)
0 1 2 3 4 5 6


    fibo(n)
    print(zero[n], one[n])