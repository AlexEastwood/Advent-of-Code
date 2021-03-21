numbers = [row.strip() for row in open("test_input.txt", encoding="utf8").readlines()]

numbers = [ int(x) for x in numbers ]

numbers = sorted(numbers)
numbers.insert(0, 0)
numbers.append(numbers[-1] + 3)

print(numbers)


one_jolt = 0
three_jolt = 0

for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] == 1:
        one_jolt += 1
    elif numbers[i + 1] - numbers[i] == 3:
        three_jolt += 1
        
print(one_jolt * three_jolt)
values = [1, 2 ,3]

differences = [0 for x in numbers[:-1]]

for i in range(len(numbers) - 1):
    try:
        if numbers[i + 1] - numbers[i] in values:
            differences[i] += 1
    except IndexError:
        pass
    try:
        if numbers[i + 2] - numbers[i] in values:
            differences[i] += 1
    except IndexError:
        pass
    try:
        if numbers[i + 3] - numbers[i] in values:
            differences[i] += 1
    except IndexError:
        pass
        
print(differences)

total = 0
for i in range(len(differences) - 1):
    if total == 0:
        total += differences[i]
    else:
        total *= differences[i]
        
print(total)

