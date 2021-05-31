f = open('2020/day6input.txt', 'r')
data = f.read().split('\n\n')

"""PART 1
total = 0
for group in data:
    newgroup = []
    [newgroup.append(person) for person in group.split('\n')]
    grouppositiveanswers = "".join(set(''.join(newgroup)))
    count = len(grouppositiveanswers)
    total += count
print(total)"""

#PART 2

total = 0
for group in data:
    count = 0
    newgroup = []
    [newgroup.append(person) for person in group.split('\n')]
    allanswersstr = ''.join(newgroup)
    sizegroup = len(newgroup)
    setallanswerstr = set(allanswersstr)
    for char in setallanswerstr:
        if allanswersstr.count(char) == sizegroup:
            count += 1
    total += count
print(total)




