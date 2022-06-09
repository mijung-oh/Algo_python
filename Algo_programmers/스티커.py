def solution(sticker):    
    odd = 0
    even2 = 0
    even = 0
    # 스티커가 짝수일 때
    if len(sticker) % 2 == 0:
        for i in range(len(sticker)):
            if i % 2:
                odd += sticker[i]
            else:
                even += sticker[i]
    else:
        for i in range(len(sticker)-1):
            if i % 2:
                odd += sticker[i]
            else:
                # 첫 번째 원소를 포함
                even += sticker[i]
        for i in range(2, len(sticker), 2):
            even2 += sticker[i]
    
    return max(odd, max(even, even2))