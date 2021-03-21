import os

bags = [row.strip() for row in open("input.txt", encoding="utf8").readlines()]

bags_in_bags = {}

for bag in bags:
    for bag in bags:
        s = bag.split(" bags contain ")
        bag_colour = s[0]
        bag_contents = s[1]
        
        if bag_colour not in bags_in_bags:
            bags_in_bags[bag_colour] = 0
            
        if "no other bags" in bag_contents:
            bags_in_bags[bag_colour] = 1
            continue
        else:
            count = 0
            bag_contents = bag_contents.split(",")
            for colour in bag_contents:
                number_of = int(colour[0:2].strip())
                if colour[-1] == ".":
                    colour = colour[2:-1]
                else:
                    colour = colour[2:]
                    
                if number_of == 1:
                    colour = colour[:-4]
                else:
                    colour = colour[:-5]
            
                colour = colour.strip()
                if colour in bags_in_bags:
                    count += (bags_in_bags[colour] * number_of)
                else:
                    count += number_of         
            bags_in_bags[bag_colour] = count + 1
                
        
print(bags_in_bags["shiny gold"])
