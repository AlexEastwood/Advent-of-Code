import math

passes = [row.strip() for row in open('input.txt', encoding="utf8").readlines()]
seat_ids = []


for ticket in passes:
    upper_bound = 127
    lower_bound = 0
    seat_upper_bound = 7
    seat_lower_bound = 0
    rows = ticket[0:7]
    seat = ticket[7:]
    
    for i in range(len(rows) - 1):
        if rows[i] == "F":
            upper_bound = math.floor((upper_bound + lower_bound) / 2)
        else:
            lower_bound = math.ceil((upper_bound + lower_bound) / 2)         
    if rows[6] == "F":
        row = lower_bound
    else:
        row = upper_bound
    
    for i in range(len(seat) - 1):
        if seat[i] == "L":
            seat_upper_bound = math.floor((seat_upper_bound + seat_lower_bound) / 2)
        else:
            seat_lower_bound = math.ceil((seat_upper_bound + seat_lower_bound) / 2)
    if seat[2] == "L":
        seat = round(seat_lower_bound)
    else:
        seat = round(seat_upper_bound)   
    seat_id = row * 8 + seat
    seat_ids.append(seat_id)

print(max(seat_ids))

for i in range(max(seat_ids)):
    if i not in seat_ids and i - 1 in seat_ids and i + 1 in seat_ids:
        print(i)
    