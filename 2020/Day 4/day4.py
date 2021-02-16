import re
input_file = [row.strip() for row in open('input.txt', encoding="utf8").readlines()]

passports = []
entry = ""
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid_passports = []
valid_round_one = 0
valid_round_two = 0

for line in input_file:
    if line != "":
        entry = entry + " " + line
    else:
        passports.append(entry)
        entry = ""
passports.append(entry)
        
for passport in passports:
    if all(x in passport for x in fields):
        valid_passports.append(passport)
        valid_round_one += 1
        
for passport in valid_passports:
    if 1920 <= int(re.search(r"(byr:)([0-9]{4})", passport).group(2)) <= 2002:
        if 2010 <= int(re.search(r"(iyr:)([0-9]{4})", passport).group(2)) <= 2020:
            if 2020 <= int(re.search(r"(eyr:)([0-9]{4})", passport).group(2)) <= 2030:
                if re.search(r"(hcl:)(#[a-f0-9]{6})", passport):
                    if re.search(r"(pid:)([0-9]{9})", passport):
                        if len(re.search(r"(pid:[0-9]{9})", passport).group(1)) == 13:
                            try:
                                eye_colour = re.search(r"(ecl:)([a-z]{3})", passport).group(2)
                            except AttributeError:
                                continue
                            if eye_colour in eye_colours:
                                if re.search(r"(hgt:)([0-9]{2,3})(cm|in)", passport):
                                    if re.search(r"(hgt:)([0-9]{2,3})(cm|in)", passport).group(3) == "cm":
                                        if 150 <= int(re.search(r"(hgt:)([0-9]{2,3})(cm|in)", passport).group(2)) <= 193:
                                            valid_round_two += 1
                                    elif re.search(r"(hgt:)([0-9]{2,3})(cm|in)", passport).group(3) == "in":
                                        if 59 <= int(re.search(r"(hgt:)([0-9]{2,3})(cm|in)", passport).group(2)) <= 76:
                                            valid_round_two += 1

print(valid_round_two)
        

