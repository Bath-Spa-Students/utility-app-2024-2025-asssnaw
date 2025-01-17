#firstly we import the table using tabulate
from tabulate import tabulate 

#this is the main menu of my vending machine
vendingmenu={
    "Chips": { #first category of my vending machine is chips
        "S1": {"Name": "Hot Cheetos", "Price $": 1.50, "Stock": 10},
        "S2": {"Name": "Lay's", "Price $": 1.75, "Stock": 18},
        "S3": {"Name": "Fritos", "Price $": 3.00, "Stock": 15},
        "S4": {"Name": "Pringles", "Price $": 4.00, "Stock": 25},
        "S5": {"Name": "Ruffles", "Price $": 2.75, "Stock": 16},
        "S6": {"Name": "Herr's Snacks", "Price $": 2.75, "Stock": 14},
        "S7": {"Name": "Doritos", "Price $": 5.00, "Stock": 21},
    },
    "Drinks": { #second category of my vending machine is drinks
        "D1": {"Name": "Cola Diet", "Price $": 2.00, "Stock": 16},
        "D2": {"Name": "Mountain Dew", "Price $": 3.00, "Stock": 19},
        "D3": {"Name": "Cola Regular", "Price $": 2.50, "Stock": 13},
        "D4": {"Name": "Fanta", "Price $": 2.95, "Stock": 12},
        "D5": {"Name": "Mango Juice", "Price $": 1.00, "Stock": 18},
        "D6": {"Name": "Water", "Price $": 2.00, "Stock": 19},
        "D7": {"Name": "Soda", "Price $": 1.75, "Stock": 14},
        "D8": {"Name": "Sprite", "Price $": 2.50, "Stock": 11},
    },
    "Chocolates": { #third category of my vending machine is chocolates
        "C1": {"Name": "Milky Bar", "Price $": 1.00, "Stock": 13},
        "C2": {"Name": "Kinder Bites", "Price $": 2.50, "Stock": 15},
        "C3": {"Name": "kunafa Chocolate Bar", "Price $": 7.00, "Stock": 10},
        "C4": {"Name": "KitKat", "Price $": 1.75, "Stock": 12},
        "C5": {"Name": "Cadbury", "Price $": 7.75, "Stock": 16},
        "C6": {"Name": "Lindt", "Price $": 5.25, "Stock": 15},
        "C7": {"Name": "Dairy Milk", "Price $": 5.00, "Stock": 11},
        "C8": {"Name": "Toblerone", "Price $": 5.25, "Stock": 12},
    },
    "Ice-Cream Bars": { #fourth category of my vending machine is ice cream bars
        "I1": {"Name": "Creamsicle Bar", "Price $": 2.00, "Stock": 18},
        "I2": {"Name": "Candy Center Bar", "Price $": 3.00, "Stock": 16},
        "I3": {"Name": "Choclate Eclair Bar", "Price $": 4.00, "Stock": 17},
        "I4": {"Name": "Strawberry Shortcake Bar", "Price $": 3.75, "Stock": 15},
        "I5": {"Name": "Cookies & Creme Bar", "Price $": 5.50, "Stock": 13},
        "I6": {"Name": "Orignal Ice Cream Bar", "Price $": 3.95, "Stock": 18},
        "I7": {"Name": "Mint Chocolate Chip Bar", "Price $": 4.50, "Stock": 17},
    },
    "Candies": { #fifth category of my vending machine is candies
        "H1": {"Name": "Gummies", "Price $": 3.50, "Stock": 12},
        "H2": {"Name": "Hard Candy", "Price $": 1.95, "Stock": 14},
        "H3": {"Name": "Sour Patch", "Price $": 2.75, "Stock": 16},
        "H4": {"Name": "Stick Candy", "Price $": 3.95, "Stock": 12},
        "H5": {"Name": "Jelly Beans", "Price $": 1.25, "Stock": 19},
        "H6": {"Name": "Skittles", "Price $": 3.95, "Stock": 17},
        "H7": {"Name": "Mints", "Price $": 2.25, "Stock": 13},
        "H8": {"Name": "Lollipop", "Price $": 1.00, "Stock": 11},
    },
    "Cookies": { #sixth category of my vending machine is cookies
        "H1": {"Name": "Chocolate Chip cookies", "Price $": 3.50, "Stock": 12},
        "H2": {"Name": "Sugar cookies", "Price $": 1.95, "Stock": 14},
        "H3": {"Name": "Gingerbread cookies", "Price $": 2.75, "Stock": 16},
        "H4": {"Name": "Macarons", "Price $": 3.95, "Stock": 12},
        "H5": {"Name": "Butter Cookies", "Price $": 1.25, "Stock": 19},
        "H6": {"Name": "Crinkle Cookies", "Price $": 3.95, "Stock": 17},
        "H7": {"Name": "Gingersnaps", "Price $": 2.25, "Stock": 13},
        "H8": {"Name": "Oatmeal Cookies", "Price $": 1.00, "Stock": 11},
    },
    "Hot-Beverages": { #seventh category of my vending machine is hot beverages
        "I1": {"Name": "Hot Choclate", "Price $": 2.00, "Stock": 18},
        "I2": {"Name": "Tea", "Price $": 1.00, "Stock": 16},
        "I3": {"Name": "Irish coffee", "Price $": 2.00, "Stock": 17},
        "I4": {"Name": "caffe mocha", "Price $": 3.75, "Stock": 15},
        "I5": {"Name": "Turmeric latte", "Price $": 4.50, "Stock": 13},
        "I6": {"Name": "Espresso", "Price $": 2.95, "Stock": 18},
        "I7": {"Name": "Pumpkin Spice Latte", "Price $": 4.50, "Stock": 17},
    },
}

#following code is used to display vending machine in a table format
def display_vendingmenu(category=None):
    Vendingmac_tabledata = []
    if category:
        items = vendingmenu.get(category, {})
        for code, item in items.items():
            stock_stat = f"{item['Stock']}" if item['Stock'] > 0 else "Out of stock"
            Vendingmac_tabledata.append([code, item["Name"], f"${item['Price $']:.2f}", stock_stat])
        return tabulate(Vendingmac_tabledata, headers=["Code", "Item", "Price", "Stock"], tablefmt="pretty")
    else:
        categories = list(vendingmenu.keys())
        Vendingmac_tabledata = [[i + 1, cat] for i, cat in enumerate(categories)]
        return tabulate(Vendingmac_tabledata, headers=["Code", "Category"], tablefmt="pretty")

#the following code is used to function the customization for hot beverages    
def custom_hot_bev():
    sugar = input("Would you like to add sugar? (yes/no): ").strip().lower() == "yes"
    milk = input("Would you like to add milk? (yes/no): ").strip().lower() == "yes"
    print(f"Hot Beverage customized: {'Sugar added' if sugar else 'No sugar added'}, {'Milk added' if milk else 'No milk added'}.\n") 

#Following code is written to run the main program
if __name__ == "__main__":
    print("Welcome to the Vending Machine!!!!")
    totalcost = 0
    categories = list(vendingmenu.keys())
    while True:
        print("\n--- Categories ---")
        print(display_vendingmenu())
        category_code = input("Choose a category for the code (or type 'exit' to finish): ").strip()
        if category_code.lower() == "exit":
            break

        if not category_code.isdigit() or int(category_code) < 1 or int(category_code) > len(categories):
            print("Invalid code entered. Please try again.")
            continue

        category = categories[int(category_code) - 1]
        print(f"\n--- {category} Menu ---")
        print(display_vendingmenu(category))
        code = input("Enter the item code of the item to purchase (or type 'back' to go to categories): ").strip().upper()
        if code.lower() == "back":
            continue

        item = vendingmenu[category].get(code)
        if not item:
            print("Invalid code entered. Please try again.")
            continue

        if item["Stock"] <= 0:
            print(f"Sorry, {item['Name']} is currently out of stock.")
            continue

        if category == "7":
            custom_hot_bev()

        totalcost += item["Price $"]
        item["Stock"] -= 1
        print(f"Added {item['Name']} to your cart. your current total is: ${totalcost:.2f}")

    if totalcost > 0:
        print(f"\nYour total cost is: ${totalcost:.2f}")
        while True:
            payment = float(input("Enter the amount to be paid: $"))
            if payment >= totalcost:
                change = payment - totalcost
                print(f"Payment was successful! Your change: ${change:.2f}")
                break
            else:
                print(f"The payment done is insufficient. You still owe me ${totalcost - payment:.2f}.")
    else:
        print("No items purchased. See you next time!")

    print("Thank you for using the Vending Machine, Have a good day!")
