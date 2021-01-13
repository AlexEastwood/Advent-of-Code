text_file = open("input.txt", "r")
slope = text_file.readlines()


x = 3
y = 1
trees = []

while y < len(slope):
    try:
        trees.append(slope[y][x])
    except IndexError:
        x = x - len(slope[y])
        continue
    x += 3
    y += 1
    
trees_string = "".join(trees)
print(trees_string.count("#"))