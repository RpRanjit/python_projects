# a - z (lower case)
# 0 - 9
# . _ 1 at time
# @ 1 at time
# . in 2 or 3 position
# ^ as the first character in that string
# \ search the content in the string
# ? is work as 0 and 1 if there is more than  1 it represent false
# \w search that character in whole string
# if we want to search a character in particular position than we use {} bracket
# $ is use for search from reverse


import re

email_condition = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

while True:
    user_choice = int(input('''
            1 for checking email.
            2 for exit
        '''))
    if user_choice == 1:
        user_email = input(" Enter your email: ")
        if re.search(email_condition, user_email):
            print("Right Email")
        else:
            print("Wrong Email")
    elif user_choice == 2:
        break
    else:
        print("Invalid Input")