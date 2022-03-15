def solution(N, number):
    # 이전 값에만 영향을 받기 때문에 모든 경우의 수를 탐색할 필요는 없다.
    
    # 숫자로만 이루어진 것을 설정
    allNumbers = [set() for _ in range(8)]
    for i in range(8):
        allNumbers[i].add(int(str(N) * (i+1)))
        
    