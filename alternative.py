'''
# Pseudo Code.
1 - Take string input from user and save it into my_string variable.
2 - Define empty string variable alternate_string = ""
3 - Run for loop on my_string for i in range(len(my_string)):
4 - Check if i % 2 == 0, then change character of that position to upper case and save it into alternate_string variable.
5 - Else change character of that position to lower case and save it into alternate_string variable.
6 - Print alternate_string.

# Part 2
1 - Take string input from user and save it into new_string variable.
2 - Define empty string variable new_word = ""
3 - Define character = 1 variable.
4 - Run for loop on or i in new_string.split()
5 - check if character != 1, then add empty space in new_string.
6 - Check if i % 2 == 0, then change word of that position to upper case and save it into new_string variable.
7 - Else change character of that position to lower case and save it into new_string variable.
8 - then increment character by 1.
9 - Print new_string.
'''
print("--------------Each character change into upper case and lower case -------------------")
print()
user_input_string = input("Please enter a string: ")

alternate_string = "" # String to store the string with alternate characters capital and small

for i in range(len(user_input_string)):
    if i % 2 == 0:
        alternate_string = alternate_string + user_input_string[i].upper()

    else:
        alternate_string = alternate_string + user_input_string[i].lower()
print(alternate_string)

print("--------------Each Word change into upper case and lower case -------------------")
print()
new_string = input("Please enter a string: ")
new_word = ""
character = 1

for i in new_string.split():
    if character != 1:
        new_word += " "
    if character % 2 == 0:
        new_word += i.upper()
    
    else:
        new_word += i.lower()
    character += 1
print(new_word)
print("----------------------------------------------------------------------------------")