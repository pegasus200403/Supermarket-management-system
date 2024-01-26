def Electronics():
    global elecitem
    aelecitem = 0
    belecitem = 0
    celecitem = 0
    delecitem = 0
    eelecitem = 0
    felecitem = 0

    print("WELCOME TO ELECTRONICS FACILITY")
    print("ITEMS AVAILABLE ARE:")
    print("1. Microwave Oven - Rs 10000")
    print("2. Toaster - Rs 5000")
    print("3. Grinder - Rs 3000")
    print("4. Samsung s10 - Rs 100000")
    print("5. Apple iPhone 11 Pro - Rs 120000")
    print("6. Voltas A/C - Rs 50000")
    print("Press 7 for exit")

    while True:
        x = int(input("---Please choose item no---"))

        if x == 1:
            d = int(input("Please enter quantity"))
            aelecitem += d * 10000
            print("Price of Microwave Oven =", aelecitem)
        elif x == 2:
            d = int(input("Please enter quantity"))
            belecitem += d * 5000
            print("Price of Toaster =", belecitem)
        elif x == 3:
            d = int(input("Please enter quantity"))
            celecitem += d * 3000
            print("Price of Grinder =", celecitem)
        elif x == 4:
            d = int(input("Please enter quantity"))
            delecitem += d * 100000
            print("Price of Samsung s10 =", delecitem)
        elif x == 5:
            d = int(input("Please enter quantity"))
            eelecitem += d * 120000
            print("Price of Apple iPhone 11 Pro =", eelecitem)
        elif x == 6:
            d = int(input("Please enter quantity"))
            felecitem += d * 50000
            print("Price of Voltas A/C =", felecitem)
        elif x == 7:
            break
        else:
            print("Match not found")

    elecitem = aelecitem + belecitem + celecitem + delecitem + eelecitem + felecitem
    print("Total cost at Electronic items =", elecitem)
    return elecitem

# Similar modifications for other departments (Grocery, Cafe, Kitchen, Vegetable)...

def entry():
    st = []
    n = int(input("Enter the Total Record number you want to enter"))
    for x in range(n):
        roll = int(input("Enter the Id number:"))
        nam = input("Enter the staff name")
        sal = int(input("salary in rupees"))
        st.append([roll, nam, sal])

    import pickle
    f = open("staff.dat", "wb")
    pickle.dump(st, f)
    f.close()

# Similar modifications for other functions (display, delete, modify)...

print("-------WELCOME TO BHAT BHATENI SUPERMARKET -------")
print("*****HAPPINESS LIES HERE*****")

while True:
    a = int(input("Enter 1 for Customer service or Press 2 for Administration service or Press 3 for EXIT"))

    if a == 1:
        print("---BHAT BHATENI WELCOMES YOU TO SELF CUSTOMER BILLING CENTER---")
        elecitem = 0
        groitem = 0
        cafeitem = 0
        kititem = 0
        vegitem = 0

        while True:
            print("--Please select your product facility--")
            print("Press 1. For Electronic Department")
            print("Press 2. For Grocery Department")
            print("Press 3. For Cafe Billing")
            print("Press 4. For Kitchen Utensils Department")
            print("Press 5. For Vegetable shop")
            print("Press 6. For EXIT")

            n = int(input("Please enter your choice"))

            if n == 1:
                Electronics()
            # Similar modifications for other departments (Grocery, Cafe, Kitchen, Vegetable)...

            elif n == 6:
                break
            else:
                print("Wrong output")

        total = elecitem + groitem + cafeitem + kititem + vegitem
        print("Your Total Amount=Rs", total)

    elif a == 2:
        print("Hi Admin Sir Welcome to Staff Details")
        p = int(input("Enter the password"))

        if p == 1234:
            print("Please first entry your data of staff")
            entry()

            while True:
                n = int(input("Do you want Delete a person record press 1 or press 2 for modifying salary or press 3 to exit"))

                if n == 1:
                    delete()
                elif n == 2:
                    modify()
                elif n == 3:
                    print("THANK YOU")
                    break
                else:
                    print("Wrong input")

    elif a == 3:
        print("Thank You, Have a Good Day")
        break

    else:
        print
