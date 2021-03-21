lines = [row.strip() for row in open("input.txt", encoding="utf8").readlines()]

i = 0
j = 0
jmp_nop = 0

for line in lines:
    instruction = line.split(" ")[0]
    if instruction == "jmp" or instruction == "nop":
        jmp_nop += 1

for k in range(jmp_nop):
    done = []
    acc = 0
    i = 0
    while True:
        if i in done:
            j = 0 
            print(acc)
            break
        else:
            try:
                done.append(i)
                instruction = lines[i].split(" ")[0]
                value = int(lines[i].split(" ")[1])
            except IndexError:
                print(acc)
                exit()
            
            if instruction == "nop" and k == j:
                instruction = "jmp"
            elif instruction == "jmp" and k == j:
                instruction = "nop"

            if instruction == "nop":
                j += 1
                i += 1
                continue
            elif instruction == "acc":
                acc += value
                i += 1
                continue
            else:
                j += 1
                i += value
                continue