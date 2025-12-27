import random

# List of who or what
subjects = ["Dwayne Johnson", "A group of Monkey", "Indira Gaandi", "K.P Sharma Oli", "Salman Khan"]
# list of action
actions = ["launche missile", "cancels", "dances with", "eats", "declares war on"]
# list of places or things
objects = ["at the Red Fort", "in Kathmandu Dharara", "a plate of momos","inside parliaments", " at Ram Ghat"]

while True: 
    choose = input('''Yes, if you want to continue
No, if you want ti exit : ''').strip()
    if choose.lower() == "yes":
        user_choice = input('''Do you have someone name, action or place on for mind for whom you want to create fake news:
                            Yes, if you want to continue
                            No, if you want ti exit : ''').strip()
        if user_choice.lower() == "yes":
            name= input("Enter the name: ")
            action = input("Write the ction: ")
            place = input("Enter the place name: ")
            if not name:
                name = random.choice(subjects)
            if not action: 
                action = random.choice(actions)
            if not place:
                place = random.choice(objects)
            sentence = f"Breaking NEWS: {name} {action} {place}."
        elif user_choice.lower() == "no":
            sentence = f"Breaking NEWS: {random.choice(subjects)} {random.choice(actions)} {random.choice(objects)}."
        else:
            print("Invalid Input. Try again")
            break
        print()
        print(sentence)
        print()
    elif choose.lower() == "no":
        print("Good Bye")
        break
    else: 
        print("Invalid Input")