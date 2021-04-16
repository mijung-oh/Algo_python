def bin_to_dec(lst):
    c = 0
    result = 0
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == 1:
            result += 2 ** c
        c += 1
    return result

def three_to_dec(lst):
    c = 0
    result = 0
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == 0:
            c += 1
            continue
        result += lst[i] * (3 ** c)
        c += 1
    return result

T = int(input())
for tc in range(1, T+1):
    binary = list(map(int, input()))
    three = list(map(int, input()))
    result = 0
    for i in range(len(binary)):
        # change binary 1 bit
        binary[i] = 0 if binary[i] else 1
        binary_V = bin_to_dec(binary)
        for j in range(len(three)):
            pre = three[j]
            for k in range(3):
                if three[j] == k: continue
                three[j] = k
                three_V = three_to_dec(three)
                if binary_V == three_V:
                    result = binary_V
                    break
            # 원상복귀
            if result:
                break
            three[j] = pre
        binary[i] = 0 if binary[i] else 1

            
        if result:
            break
    print('#{} {}'.format(tc, result))

