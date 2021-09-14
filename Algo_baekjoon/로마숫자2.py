a = input()
b = input()

roma = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}
roma_cnt = {
    "M": 0,
    "D": 0,
    "C": 0,
    "L": 0,
    "X": 0,
    "V": 0,
    "I": 0
}
small_first = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}
roma_list = [[1000, "M", 0], [500, "D", 0], [100, "C", 0], [50, "L", 0], [10, "X", 0], [5, "V", 0], [1, "I", 0]]

# 아라비아숫자로 변경하기
def charToNumber(a):
    sub_sum = 0
    i = 0
    while i < len(a):
        # 작은 값이 먼저인 경우
        if i+1 < len(a) and a[i:i+2] in small_first.keys():
            sub_sum += small_first[a[i:i+2]]
            i += 2
        else:
            sub_sum += roma[a[i]][0]
            i += 1
    return sub_sum
    

# 로마 숫자로 변경하기
def NumberToChar(n):
    result = ""
    cnt = { "M": 0, "I": 0, "X": 0, "C": 0}

    string_n = str(n)
    for i in range(len(string_n)):
        curV = int(string_n[i]) * (10 ** (len(string_n) - 1 - i))
        check = 1
        # 해당 숫자가 로마숫자인 경우
        for key, value in roma.items():
            if curV == value[0]:
                result += key
                check = 0
                break
        # small first가 아닌 경우 
        if check:
            for key, value in small_first.items():
                if curV == value:
                    result += key
                    check = 0
                    break
        
        # 둘 다 아닌 경우, 로마숫자 여러개로 만든다.
        if check:
            if curV >= 1000:
                if curV // 1000 > 3:
                    result += "M" * 3
                    result += "D" * (curV//1000 - 3) * 2
            elif curV >= 500:
                result += "D"
                if (curV - 500) // 100 < 4:
                    result += "C" * ((curV - 500) // 100)
                # 500 + 400
                else:
                    result += "CD"
            elif curV >= 100:
                
                    
    return result
                

        
        
    
    return result

        

a_sum = charToNumber(a)
b_sum = charToNumber(b)
total_sum = a_sum + b_sum
