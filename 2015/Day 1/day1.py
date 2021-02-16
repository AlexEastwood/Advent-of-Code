with open("C:/Users/Alex - Programming/Desktop/Projects/Advent/Advent-of-Code/2015/Day 1/input.txt", "r") as file:
    floors = file.read()
    
floor = 0
for i in range(len(floors)):
    if floors[i] == "(":
        floor += 1
    else:
        floor -= 1
        if floor == -1:
            print(i + 1)
            exit()