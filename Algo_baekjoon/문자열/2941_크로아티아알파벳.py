croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
words = input()

for c in croatia:
    words = words.replace(c, "*")
    
print(len(words))