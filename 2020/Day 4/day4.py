import re
input_file = [row.strip() for row in open('input.txt').readlines()]

passports = []
entry = ""
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0

for line in input_file:
    if line != "":
        entry = entry + " " + line
    else:
        passports.append(entry)
        entry = ""
passports.append(entry)
        
for passport in passports:
    if all(x in passport for x in fields):
        valid += 1
        
print(valid)