import re
with open('2020/day4input.txt', 'r') as f:
    data = f.read().split("\n\n")
    for i in range(len(data)):
        data[i] = re.split('[ \n]', data[i])

for i in range(len(data)):
    data[i] = {elements.split(':')[0]:elements.split(':')[1] for elements in data[i]}

def is_match(regex, stringvalue):
    matched = re.match(regex, stringvalue)
    return bool(matched)

#PART 1
"""total = 0

for line in data:
    count = 0
    needed_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    line_keys = line.keys()
    isValid = True
    for key in needed_keys:
        if key not in line_keys:
            isValid = False
    if isValid:
        total += 1

print(total)"""

#PART II

def check(key, line):
    if key not in line.keys():
        return False
    if key == 'byr':
        matched = re.match('^[0-9]{4}$', line[key])
        if not bool(matched):
            return False
        if 1920 <= int(line[key]) <= 2002:
            return True
        return False
    if key == 'iyr':
        matched = re.match('^[0-9]{4}$', line[key])
        if not bool(matched):
            return False
        if 2010 <= int(line[key]) <= 2020:
            return True
        return False
    if key == 'eyr':
        matched = re.match('^[0-9]{4}$', line[key])
        if not bool(matched):
            return False
        if 2020 <= int(line[key]) <= 2030:
            return True
        return False
    if key == 'hgt':
        matched = re.match('^[0-9]+(cm|in)$', line[key])
        if not bool(matched):
            return False
        if line[key][-2:] == "cm":
            if 150 <= int(line[key][:-2]) <= 193:
                return True
        if line[key][-2:] == "in":
            if 59 <= int(line[key][:-2]) <= 76:
                return True
        return False
    if key == 'hcl':
        matched = re.match('^#[0-9a-f]{6}$', line[key])
        if not bool(matched):
            return False
        if bool(matched):
            return True
    if key == 'ecl':
        return line[key] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if key == 'pid':
        matched = re.match('^[0-9]{9}$', line[key])
        return bool(matched)

"""
data = [{"ecl":"gry", "pid":"860033327", "eyr":"2020","hcl":"#fffffd", "byr":"1937" ,"iyr":"2017", 'cid':'147', 'hgt':'183cm'},
{'iyr':'2013', 'ecl':'amb', 'cid':'350' ,'eyr':'2023' ,'pid':'028048884','hcl':'#cfa07d' ,'byr':'1929'},
{'hcl':'#ae17e1', 'iyr':'2013', 'eyr':'2024' ,'ecl':'brn', 'pid':'760753108', 'byr':'1931', 'hgt':'179cm'},
{'hcl':'#cfa07d', 'eyr':'2025', 'pid':'166559648', 'iyr':'2011', 'ecl':'brn', 'hgt':'59in'}]
"""

"""data = [
    {'pid':'087499704', 'hgt':'74in', 'ecl':'grn', 'iyr':'2012', 'eyr':'2030', 'byr':'1980', 'hcl':'#623a2f'},
    {'eyr':'2029', 'ecl':'blu','cid':'129234567', 'byr':'1989', 'iyr':'2014', 'pid':'896056539', 'hcl':'#a97842', 'hgt':'165cm'},
    {'hcl':'#888785', 'hgt':'164cm', 'byr':'2001', 'iyr':'2013', 'cid':'88', 'pid':'545766238', 'ecl':'hzl', 'eyr':'2022'},
    {'iyr':'2010', 'hgt':'158cm', 'hcl':'#b6652a', 'ecl':'blu', 'byr':'1944', 'eyr':'2021', 'pid':'093154719'}
]"""


total = 0
for line in data:
    needed_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    validpassport = True
    for key in needed_keys:
        if not check(key, line):
            validpassport = False
    if validpassport:
        #print(line)
        total += 1
    
print(total)
    






