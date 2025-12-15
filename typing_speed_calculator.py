from time import *
import random


def mistake(pragtest, usertest):
    error = 0
    for i in range(len(pragtest)):
        try:
            if pragtest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed(initial_time, end_time, user_input):
    time_delay = end_time - initial_time
    time_round = round(time_delay, 2)
    speed = len(user_input) / time_round
    return round(speed)
        

while True:
    user_choice = input("Do you want to check you typing speed yes/no:")
    if user_choice.lower() == "yes":
        test = ["Global markets steady as investors monitor inflation and central bank signals. Gaza humanitarian situation worsens amid ongoing fighting and aid shortages.",
                "Ukraine conflict continues as diplomatic talks show limited progress. Tech firms expand artificial intelligence tools for business and education.",
                "Severe weather warnings issued after storms disrupt transport and power supplies.",
                "How are you?"]

        test1 = random.choice(test)
        print("***** typing test *****")
        print(test1)
        print()
        print()
        time_1 = time()
        test_input = input("Enter : ")
        time_2 = time()

        print()
        print()
        print("Speed :",speed(time_1, time_2, test_input), "w/s")
        print("Error :",mistake(test1, test_input))
    elif user_choice.lower() == "no":
        break
    else:
        print("Invalid Input")
