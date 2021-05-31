with open('2020/day1input.txt', 'r') as f:
    data = f.readlines()
    data = [int(num) for num in data]
    print(data)


for i in range(len(data)-2):
    for j in range(i+1,len(data)-1):
        for k in range(j+1, len(data)):
            if data[i] + data[j] + data[k]== 2020:
                print(data[i], data[j], data[k])
                print(data[i]*data[j]*data[k])
            
