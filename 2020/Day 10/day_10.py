numbers = [row.strip() for row in open("input.txt", encoding="utf8").readlines()]

numbers = [ int(x) for x in numbers ]

numbers = sorted(numbers)
numbers.insert(0,0)
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

differences = {}
for i in range(len(numbers)):
    differences[numbers[i]] = 0

differences[numbers[-1]] = 1

print(differences)
    
for i in range(2, len(numbers) + 1):
    total = 0
    if numbers[-i] + 1 in differences:
        total += differences[numbers[-i] + 1]
    if numbers[-i] + 2 in differences:
        total += differences[numbers[-i] + 2]
    if numbers[-i] + 3 in differences:
        total += differences[numbers[-i] + 3]
        
    differences[numbers[-i]] = total
    
print(differences)
print(max(differences.values()))