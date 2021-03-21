numbers = [row.strip() for row in open("input.txt", encoding="utf8").readlines()]

numbers = [ int(x) for x in numbers ]

preamble = numbers[:25]


for k in range(25, len(numbers)):
    values = []
    for j in range(len(preamble)):
        for i in range(len(preamble)):
            if i != j:
                values.append(preamble[j] + preamble[i])
    
    if numbers[k] in values:
        preamble.pop(0)
        preamble.append(numbers[k])
        continue
    else:
        weakness = numbers[k]
        break
    
value_range = 1

while True:
    starting_value = 0
    ending_value = starting_value + value_range
    while ending_value < len(numbers):
        if (sum(numbers[starting_value:ending_value + 1])) == weakness:
            print(max(numbers[starting_value:ending_value]) + min(numbers[starting_value:ending_value]))
            exit()
        else:
            print(numbers[starting_value] + numbers[ending_value])
            starting_value += 1
            ending_value += 1
    
    value_range += 1
        



