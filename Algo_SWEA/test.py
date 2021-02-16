a = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

t=[]
for i in range(3):
    t.append([k[i] for k in a])
    

# print(t)
# for i in range(3):
#     print(sum(t[i]))

print(*a[0])