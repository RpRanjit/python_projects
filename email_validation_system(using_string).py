# Email valiation system by using string methods

email = input("Enter your email: ")#g@g.in g@g.com
a,b,c = 0, 0, 0
if len(email) >= 6: #1
    if email[0].isalpha(): #2
        if ("@" in email) and (email.count("@") == 1): #3
            if (email[-3] != ".") ^ (email[-4] != "."): #4
                for i in email:
                    if i == i.isspace(): #5
                        a = 1
                    elif i.isalpha():
                        if i == i.upper(): #5
                            b = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else: #5
                        c = 1

                if a == 1 or b == 1 or c == 1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4.")
        else:
            print("Wrong Email 3.")
    else:
        print("Wrong Email 2.")
else:
    print("Wrong Email 1.")