N = int(input())
people = list(map(int, input().split()))
B, C = map(int, input().split())

result = len(people)
for p in people:
    a = (p-B) // C + 1 if (p-B) % C else (p-B) // C
    if a > 0:
        result += a
print(result)