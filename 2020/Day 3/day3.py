
with open("input.txt", "r") as file:
    slope = [line.rstrip() for line in file]

def ski_run(speed, drop):
    x = 0
    y = 0
    trees = 0

    while y < len(slope):
        if slope[y][x % len(slope[0])] == "#":
            trees += 1
            
        x += speed
        y += drop
    
    return trees

sum = ski_run(1, 1) * ski_run(3, 1) * ski_run(5, 1) * ski_run(7, 1) * ski_run(1, 2)

print(sum)