import time
f = open('2020/day7input.txt', 'r')
data = f.read().split('\n')


for i in range(len(data)):
    End = False
    data[i] = data[i].split(" bags contain ")
    if data[i][1] == 'no other bags.':
        End = True
    if not End:
        data[i][1] = data[i][1].split(', ')
        for j in range(len(data[i][1])):
            if data[i][1][j][-1] == '.':
                data[i][1][j] = data[i][1][j][:-1]
            if data[i][1][j][-1] != 's':
                data[i][1][j] += 's'
            data[i][1][j] = data[i][1][j][2:-5]
dictforline = {data[i][0]:[bagname for bagname in data[i][1]] for i in range(len(data)) if  not data[i][1] == 'no other bags.'}

def explore(key,dictionary):
    total = 0
    if key not in [keyy for keyy in dictionary.keys()]:
        return None
    elif "shiny gold" in dictionary[key]:
        return True
    else:
        for element in dictionary[key]:
            if explore(element,dictionary) != None:
                return True
t0 = time.time()
total = 0
for key in dictforline.keys():
    if explore(key, dictforline):
        total += 1
print(total, time.time() - t0)

def explore(key,dictionary,store):
    if key in store.keys():
        return store[key]
    if key not in [keyy for keyy in dictionary.keys()]:
        return None
    elif "shiny gold" in dictionary[key]:
        return True
    else:
        for element in dictionary[key]:
            store[element] = explore(element,dictionary,store)
            if store[element] != None:
                return True
t1 = time.time()
store = {}
total = 0
for key in dictforline.keys():
    if explore(key, dictforline,store):
        total += 1
print(total, time.time() - t1)

#Very very cool. I used the dynamic programming trick to divide time 100fold. 

