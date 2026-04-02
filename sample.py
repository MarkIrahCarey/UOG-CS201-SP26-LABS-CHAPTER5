category_to_items = {
    "snacks": [
        ["Potato Chips", 2.49],
        ["Chocolate Bar", 1.99],
        ["Instant Noodles", 1.25],
        ["Gummy Bears", 2.99],
        ["Cookies", 3.49],
        ["Beef Jerky", 4.25]
    ],
    "drinks": [],
    "food": [],
    "school supplies": [],
    "merch": []
}

best_buy = {"mobile" : [["Iphone", 399]],
            "video games" : [["slay the spire 2", 24.99]]}

def store_manager(items):
    cart = {}
    print("Hello, welcome to the UOG Bookstore! ")

    while True:
        print ("Category: ", end = "")
        for key in items: # [snacks, drinks, food, school supplies, merch]
            print (key, end = " | ")

        category = input("\nWhat category would you like? (Enter purchase to to buy what is in cart)")
        category = category.lower()

        # validate input
        if category.lower() == "purchase":
            sum = 0
            for category in items:
                for item in items[category]:
                    if item[0] in cart:
                        sum += cart[item[0]] * item[1]
            
            print (f"{round(sum, 2)}")
            break
        
        elif category not in items.keys():
            while category not in items.keys():
                category = input("INVALID, please enter the correct category: ")
        
        # shopping spree
        while True:
            for item_cat in items[category]:
                print (f"{item_cat[0]}, ${item_cat[1]}", end = " | ")
            
            # ask user for item to buy
            what_user_wants_to_buy = input("What item would you want to buy (enter exit to go back): ")

            if what_user_wants_to_buy.lower() == "exit":
                break

            item_list = []
            for item in items[category]:
                item_list.append(item[0])
            
            print(item_list)

            what_user_wants_to_buy = what_user_wants_to_buy.title()
            if what_user_wants_to_buy not in item_list:
                while what_user_wants_to_buy not in item_list:
                    what_user_wants_to_buy = input("INVALID, please enter the correct item: ").title()
            
            amount = int(input("How many would you like to buy: "))
            while amount <= 0:
                amount = int(input("INVALID, try again: "))

            if what_user_wants_to_buy is not cart:
                cart[what_user_wants_to_buy] = amount
            else:
                cart[what_user_wants_to_buy] += amount
    


store_manager(category_to_items)


