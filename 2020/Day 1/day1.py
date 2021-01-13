text_file = open("input.txt", "r")
numbers = text_file.readlines()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(len(numbers)):
    for j in range(1, len(numbers)):
        for k in range(2, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
                exit()
            k += 1
        j += 1
    i += 1