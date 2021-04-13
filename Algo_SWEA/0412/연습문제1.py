data = input()
def numTobit(s):
    t = 0
    for i in range(7):
        t = (t<<1) | (int(s[i]) - int('0'))
    print(t, end=' ')

    

for k in range(0, len(data), 7):
    numTobit(data[k:k+7])
