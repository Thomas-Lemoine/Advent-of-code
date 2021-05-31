with open('2020/day5input.txt', 'r') as f:
    data = f.read().split('\n')

listofpasses = []
maxseatID = 0
for line in data:
    row = line[:7].replace('B', '1').replace('F', '0')
    row = int(row,2)
    column = line[7:].replace('R', '1').replace('L', '0')
    column = int(column,2)
    seatID = row * 8 + column
    listofpasses.append(seatID)
    if seatID > maxseatID:
        maxseatID = seatID
        #print(f'{row}th row, {column}th column, seat ID {seatID}.')

for i in range(0,1123):
    if i not in listofpasses:
        print(i)

