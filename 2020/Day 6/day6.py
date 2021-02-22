import string

answers = []
alphabet = list(string.ascii_lowercase)
total = 0

with open('C:/Users/howarde/Documents/GitHub/Advent-of-Code/2020/Day 6/input.txt') as fp:
    contents = fp.read()
    for entry in contents.split('\n\n'):
        answers.append(entry)

for answer in answers:
    subtotal = 0
    answer = answer.split("\n")
    for i in range(len(answer[0])):
        for j in range(len(answer)):
            if answer[0][i] in answer[j]:
                if j + 1 == len(answer):
                    subtotal += 1
                else:
                    continue
            else:
                break
    
    total += subtotal
            
    
print(total)



    
