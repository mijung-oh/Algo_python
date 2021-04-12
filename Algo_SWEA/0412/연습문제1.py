data = input()
print(data)
def numTobit(s):
    t = 0
    for i in range(7):
        print('i, t', i, t)
        t = (t<<1) | (int(s[i]) - int('0'))
    print(t, end=' ')

    

# for k in range(0, len(data), 7):
    # print(numTobit(data[k:k+7])) 

print(int('1'))
print(int('1') - int('0'))