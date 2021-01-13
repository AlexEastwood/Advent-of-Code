text_file = open("input.txt", "r")
passwords = text_file.readlines()

valid_passwords = []

for password in passwords:
    password = password.split(" ")
    password_range = password[0].split("-")
    password_letter = password[1][:-1]
    password_string = password[2]
    
    if password_string[int(password_range[0]) - 1] == password_letter:
        if password_string[int(password_range[1]) - 1] != password_letter:
            valid_passwords.append(password)
    else:
        if password_string[int(password_range[1]) - 1] == password_letter:
            valid_passwords.append(password)
        
print(len(valid_passwords))