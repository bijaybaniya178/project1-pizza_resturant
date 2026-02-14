print("Welcome To Pizza House!!!")
user_name = input("ENTER YOUR NAME :")


def show_menu(file_name, menu_type):
    pizza_menu = {}

    try:
        f = open(file_name, mode='r')
        menu_items = f.readlines()
        print(f"----AVAILABLE{menu_type.upper()}")
        for item in menu_items[1:]:
            a = item.strip()
            b = item.split(",")
            pizza_menu[b[0]] = int(b[1])
    except Exception as var:
        print(var)
    else:
        f.close()

    return pizza_menu


# def order():
choice = input("Enter 1 For Veg Menu & 2 for Non-Veg menu:")

if choice == "1":
    menu = show_menu("veg_pizzas.csv", "Veg")
    for name, price in menu.items():
        print(f"     {name}= Rs{price}")
elif choice == "2":
    menu = show_menu("nonveg_pizzas.csv", "Non-Veg")
    for name, price in menu.items():
        print(f"     {name}= Rs{price}")
else:
    menu = {}
    print("--INVALID INPUT,PLEASE TRY AGAIN!!")


if not menu:
    print("Sorry, the menu is currently unavailable.")

else:

    order = []
    total_amount = 0

    while True:
        choose_pizza = input(
            "PLEASE ENTER THE PIZZA NAME TO ORDER OR QUIT TO FINISH : ").upper()
        if choose_pizza == 'QUIT':
            break
        elif choose_pizza not in menu:
            print("SORRY,THIS IS NOTS AVAILABLE .PLEASE TRY AGAIN")
            continue

        while True:
            try:
                quantity = int(input(f"ENTER QUANTITY FOR {choose_pizza}: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0!")
                    continue
                break

            except ValueError:
                print("Invalid onput! Please enter a number")

        topping_menu = show_menu("Topping.csv", "topping")
        for name, price in topping_menu.items():
            print(f"     {name}= Rs{price}")

        topping_select = []
        print("Which toppings do you want for this pizza?")
        while True:
            topping = input(
                "ENTER ONE BY ONE AND TYPE DONE ONCE YOU FINISHED: ").title()
            if topping == 'Done':
                break
            elif topping not in topping_menu:
                print("SORRY,THIS IS NOTS AVAILABLE .PLEASE TRY AGAIN")
                continue
            topping_select.append(topping)
        # print(topping_select)
        total_topping_mount = [topping_menu[i] for i in topping_select]
        total_order = menu[choose_pizza]*quantity + sum(total_topping_mount)
        total_amount += total_order
        # print(total_amount)
        order.append([choose_pizza, quantity, topping_select, total_order])

    print("~~~~~~~~~~BILL~~~~~~~~~~")
    a = 0
    for item in order:
        a += 1
        print(
            f"{a}.PIZZA={item[0]} \n  QUANTITY={item[1]} \n  TOPPINGS({item[2]} \n  Total={item[3]}")
    print(f"THE TOTAL AMOUNT : Rs.{total_amount}")
try:
    bill = open("Bill.csv", mode='a+')
    for item in order:
        bill.write(f"{user_name},{item[0]},{item[1]},{item[2]},Rs.{item[3]}\n")
    print("Bill is Saved on Bill.csv")
except Exception as a:
    print(a)
else:
    bill.close()
