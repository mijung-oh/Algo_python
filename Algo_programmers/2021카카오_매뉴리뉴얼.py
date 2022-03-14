def solution(orders, course):
    answer = []
    alphabet = [0 for _ in range(26)]
    for order in orders:
        for o in order:
            alphabet[ord(o) - ord("A")] += 1
    print(alphabet.sort())
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))