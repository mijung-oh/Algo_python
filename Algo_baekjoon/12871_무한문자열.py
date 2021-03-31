from math import gcd

s = input()
t = input()

def lcm(x, y):
    return x * y // gcd(x,y)

def isSame(s, t):    
    lcm2 = lcm(len(s), len(t))
    a = s
    b = t
    for i in range((lcm2 // len(s))-1):
        a += s
    for i in range((lcm2 // len(t)) - 1):
        b += t

    if a == b:
        return 1
    else:
        return 0

    

if len(s) == len(t):
    if s == t:
        print(1)
    else:
        print(0)
else:
    print(isSame(s, t))