"""with open('2020/day2input.txt', 'r') as f:
    data = f.read().split("\n")
    #print(data)

data = [line.split(": ") for line in data]

for line in data:
    line[0] = line[0].split()
    line[0][0] = line[0][0].split("-")

ans = 0

for line in data:
    password = line[1]
    specialchar = line[0][1]
    rangelower = int(line[0][0][0])
    rangeupper = int(line[0][0][1])
    total = 0
    for char in password:
        if char == specialchar:
            total+=1
    if rangelower <= total <= rangeupper:
        ans += 1

print(ans)"""


"""PART 2"""

with open('2020/day2input.txt', 'r') as f:
    data = f.read().split("\n")
    #print(data)

data = [line.split(": ") for line in data]

for line in data:
    line[0] = line[0].split()
    line[0][0] = line[0][0].split("-")

ans = 0

for line in data:
    password = line[1]
    specialchar = line[0][1]
    pos1 = int(line[0][0][0]) - 1
    pos2 = int(line[0][0][1]) - 1
    total = 0

    if password[pos1] == specialchar:
        total += 1
    if password[pos2] == specialchar:
        total += 1
    if total == 1:
        ans += 1

print(ans)