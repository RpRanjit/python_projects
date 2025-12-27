History_file = "text.txt"

def show_history():
    try: 
        files = open(History_file, "r")
        lines = files.readlines()
        if not lines:
            print("File is empty.")
        else:
            for line in lines:
                print(line.strip())
        files.close()
    except FileNotFoundError:
        print()
        print("File isn't created. Try to solve some equation first.")
        print()

def clear_history():
    files = open(History_file, "w")
    print("History has been cleared.")
    files.close()

def save_to_history(equation, result):
    files = open(History_file,"a")
    files.write(equation + " = " + str(result) + "\n")
    files.close()

def calculator(user_input):
    parts = user_input.split()

    # for 2 number oprations
    # if len(parts) <= 3:
    #     print("Invalid input. Enter equation in this format (e.g: 8 + 8): ")
    #     return
    # num1 = float(parts[0])
    # operator = parts[1]
    # num2 = float(parts[2])

    # for more than 2 number opreations
    if len(parts) < 3 or len(parts) % 2 == 0:
        print("Wrong Structure. Try in this format: 8 + 8 + 8")
        return
    
    try:
        result = float(parts[0])
    except:
        print("Invalid Number")
        return

    i = 1
    while i < len(parts):
        operator = parts[i]
        try: 
            num = float(parts[i + 1])
        except ValueError:
            print("Invalid Number.")
            return

        if operator == "+":
            result += num
        elif operator == "-":
            result -= num
        elif operator == "*":
            result *= num
        elif operator == "/":
            if num == "0":
                print("Dividing by zeor gives invalid output")
                return
            else:
                result /= num
        elif operator == "%":
            result %= num
        else:
            print("Invalid character/ this operation cannot be calculate.")
            return
        i += 2
    if int(result) == result:
        result = int(result)
    print("Result: ", result)
    save_to_history(user_input, result)

def main():
    print("***** Simple Calculator ****** and option for history, clear and exit.")
    while True:
        user_input = input("Enter the equations for calculation or for other functions type history, clear and exit: ")
        if user_input.lower() == "exit":
            print()
            print("Good Bye")
            break
        elif user_input.lower() == "history":
            print()
            show_history()
        elif user_input.lower() == "clear":
            print()
            clear_history()
        else:
            calculator(user_input)
main()