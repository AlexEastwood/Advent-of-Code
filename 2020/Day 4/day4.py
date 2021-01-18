with open("C:/Users/Alex - Programming/Desktop/Projects/Advent/Advent-of-Code/2020/Day 4/input.txt", "r") as file:
    passports = [line.rstrip() for line in file]
    
x = []
valid = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def check_fields(passport):
    for field in fields:
            if field not in passport:
                return False   
    return True

for passport in passports:
    if passport != "":
        x.append(passport)
    else:
        y = " ".join(x)
        if check_fields(y):
            valid += 1
        x = []

if x != []:
    y = " ".join(x)
    if check_fields(y):
        valid += 1
    x = []
        
print(valid)
    