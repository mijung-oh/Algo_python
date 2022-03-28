base = "666"
goal = int(input())
cnt = 0

while cnt < goal:
    if "666" in base:
        cnt+= 1
    base = str(int(base)+1)

print(int(base)-1)
