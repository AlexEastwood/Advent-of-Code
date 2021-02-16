with open("C:/Users/Alex - Programming/Desktop/Projects/Advent/Advent-of-Code/2020/Day 5/input.txt", "r") as file:
    passes = [line.rstrip() for line in file]
    
for ticket in passes:
    upper_bound = 127
    lower_bound = 0
    seat_upper_bound = 7
    seat_lower_bound = 0
    rows = ticket[0:7]
    seat = ticket[7:]
    i = 0
    
    for i in range(len(rows)):
        if rows[i] == "F":
            upper_bound = (upper_bound + lower_bound) / 2
        else:
            lower_bound = (upper_bound + lower_bound) / 2
            
    if rows[i] == "F":
        row = round(lower_bound)
    else:
        row = round(upper_bound)
    
    i = 0
    
    for i in range(len(seat)):
        if seat[i] == "L":
            seat_upper_bound = (seat_upper_bound + seat_lower_bound) / 2
        else:
            seat_lower_bound = (seat_upper_bound + seat_lower_bound) / 2

    if seat[i] == "L":
        seat = round(seat_lower_bound)
    else:
        seat = round(seat_upper_bound)
        
    print(row * 8 + seat)