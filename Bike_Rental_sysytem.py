class Bikeshop:
    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Total Bikes: ", self.stock)

    def rentBike(self, q):

        if q <= 0:
            print("Please enter positive value(Greater than zero): ")
        elif q > self.stock:
            print("Please enter quantity less than ", self.stock)
        else:
            self.stock -= q
            print("Total price $",q*100)
            print("Remaining stock ", self.stock)

while True: 
    uc = int(input('''
1. Display the numbers of Bike in stock.
2. Rent a bike ($100 for each bike).
3. Exit
'''))
    obj = Bikeshop(100)
    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = int(input("Enter the quantity of bike you want to rent: "))
        obj.rentBike(n)
    elif uc == 3:
        print("You choose to cancle.")
        break