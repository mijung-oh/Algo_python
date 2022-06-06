S = input()
result = [-1] * 26
for idx in range(len(S)):
    if result[ord(S[idx])-ord('a')] == -1:
        result[ord(S[idx])-ord('a')] = idx
print(*result)
