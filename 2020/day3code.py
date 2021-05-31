with open('2020/day3input.txt', 'r') as f:
    data = f.read().split("\n")

#data = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]

lstofvals = []

for num in range(1,8,2):
    row = 1
    ans = 0
    lstofthingswehit = []
    for i in range(1,len(data)):
        lengthline = len(data[i])
        row += num
        if row >= lengthline:
            row -= lengthline
        lstofthingswehit.append(data[i][row - 1])
        if data[i][row - 1] == "#":
            ans += 1
    lstofvals.append(ans)
    print(f'slope : ({num},1), {ans} collisions,\n{"".join(lstofthingswehit)}')
row = 1
ans = 0
lstofthingswehit = []
for i in range(2,len(data),2):
    lengthline = len(data[i])
    row += 1
    if row >= lengthline:
        row -= lengthline
    #print(f"row is {row - 1} line is {i}. It has value {data[i][row-1]}")

    lstofthingswehit.append(data[i][row - 1])
    if data[i][row - 1] == "#":
        ans += 1
print(f'slope : (1,2), {ans} collisions,\n{"".join(lstofthingswehit)}')
lstofvals.append(ans)
print(lstofvals)
finalanswer = 1
for ans in lstofvals:
    finalanswer *= ans
print(finalanswer)