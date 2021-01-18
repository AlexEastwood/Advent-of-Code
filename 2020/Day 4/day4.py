import ast

with open("C:/Users/Alex - Programming/Desktop/Projects/Advent/Advent-of-Code/2020/Day 4/input.txt", "r") as file:
    passports = [line.rstrip() for line in file]
    
passport_list = []
i = 0
for passport in passports:
    passport = ast.literal_eval(passport)
    print(passport)