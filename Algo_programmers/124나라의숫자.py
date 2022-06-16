def solution(n):
    init_q = { 1:"1", 2:"2", 3:"4" }
    init_r = { 0: "4", 1: "1", 2: "2" }
    
    def find(x):
        print(x)
        if x <= 3:
            return init_q[x]
        q = x // 3
        r = x % 3
        if r:
            return find(q) + init_r[r]
        else:
            return find(q-1) + init_r[r]
            
    
    return find(n)