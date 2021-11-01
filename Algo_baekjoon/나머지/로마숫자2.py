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
small_first = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

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
            sub_sum += roma[a[i]]
            i += 1
    return sub_sum
    

# 로마 숫자로 변경하기
def NumberToChar(n):
    result = ""
    string_n = str(n)
    for i in range(len(string_n)): # 2493 => 2000 400 90 3
        curV = int(string_n[i]) * (10 ** (len(string_n) - 1 - i))
        check = 1
        # 해당 숫자가 로마숫자인 경우
        for key, value in roma.items():
            if curV == value:
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
                result += "M" * (curV // 1000)

            elif curV >= 500:
                result += "D"
                result += "C" * ((curV - 500) // 100)

            elif curV >= 100:
                result += "C" * (curV // 100)

            elif curV >= 50:
                result += "L"
                result += "X" * ((curV - 50) // 10)
            
            elif curV >= 10:
                result += "X" * (curV // 10)
            
            elif curV >= 5:
                result += "V"
                result += (curV - 5) * "I"
            else:
                result += curV * "I"


                    
    return result
                
        

a_sum = charToNumber(a)
b_sum = charToNumber(b)
total_sum = a_sum + b_sum
print(total_sum)
print(NumberToChar(total_sum))