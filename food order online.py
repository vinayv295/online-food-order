class ShopData:
    def _init_(self):
        self.qunt = 0
        self.price = 0
        self.ch = 0

    def get_qunt(self):
        pass


class FoodData(ShopData):
    def get_qunt(self):
        print(f"Enter Quanties Of Your Food: ", end="")
        self.qunt = int(input())


class DrinksData(ShopData):
    def get_qunt(self):
        print(f"Enter Quanties Of Your Drink: ", end="")
        self.qunt = int(input())


class SweetsData(ShopData):
    def get_qunt(self):
        print(f"Enter Quanties Of Your Sweet: ", end="")
        self.qunt = int(input())


class Option(FoodData, DrinksData, SweetsData):
    def _init_(self):
        super()._init_()
        self.choice = 0

    def menu_list(self):
        print("choose your order category")
        print("1. FOOD")
        print("2. DRINKS")
        print("3. DESSERTS")
        self.choice = int(input("Give Your Choice Here: "))

        if self.choice == 1:
            self.food()
        elif self.choice == 2:
            self.drinks()
        elif self.choice == 3:
            self.sweets()
        else:
            print("Please choose an available choice")

    def food(self):
        print("AVAILABLE FOOD IN SHOP")
        print("Options", "Price", sep=" " * 46)
        print("1. Pizza", "329 rupees", sep=" " * 36)
        print("2. Burger", "119 ruppes", sep=" " * 34)
        print("3. Sandwich", "110 rupees", sep=" " * 32)
        self.ch = int(input("Select Your Favorite One: "))

        self.qunt = 0
        self.get_qunt()
        print("Bill DETAILED")
        if self.ch == 1:
            self.price = self.qunt * 329
            print(f"Your order is {self.qunt} Pizza")
            print(f"Amount: {self.price}")
        elif self.ch == 2:
            self.price = self.qunt * 119
            print(f"Your order is {self.qunt} Burger")
            print(f"Amount: {self.price}")
        elif self.ch == 3:
            self.price = self.qunt * 110
            print(f"Your order is {self.qunt} Sandwich")
            print(f"Amount: {self.price}")
        else:
            print("Please choose an available choice")

    def drinks(self):
        print("AVAILABLE DRINKS IN SHOP")
        print("Options", "Price", sep=" " * 46)
        print("1. Pepsi", "79 rupees", sep=" " * 36)
        print("2. Coka Cola", "69 ruppes", sep=" " * 34)
        print("3. Diet Coke", "51 rupees", sep=" " * 34)
        self.ch = int(input("Select Your Favorite One: "))

        self.qunt = 0
        self.get_qunt()
        print("Bill DETAILED")
        if self.ch == 1:
            self.price = self.qunt * 79
            print(f"Your order is {self.qunt} Pepsi")
            print(f"Amount: {self.price}")
        elif self.ch == 2:
            self.price = self.qunt * 69
            print(f"Your order is {self.qunt} Coka cola")
            print(f"Amount: {self.price}")
        elif self.ch == 3:
            self.price = self.qunt * 51
            print(f"Your order is {self.qunt} Diet Coke")
            print(f"Amount: {self.price}")
        else:
            print("Please choose an available choice")

    def sweets(self):
        print("AVAILABLE SWEETS IN SHOP")
        print("Options", "Price", sep=" " * 46)
        print("1. Gulab jamun", "110 rupees per KG", sep=" " * 28)
        print("2. Jalebi", "90 ruppes per KG", sep=" " * 32)
        print("3. Kheer", "130 rupees per KG", sep=" " * 30)
        self.ch = int(input("Select Your Favorite One: "))

        self.qunt = 0
        self.get_qunt()
        print("Bill DETAILED")
        if self.ch == 1:
            self.price = self.qunt * 110
            print(f"Your order is {self.qunt} Gulab jamun")
            print(f"Amount: {self.price}")
        elif self.ch == 2:
            self.price = self.qunt * 90
            print(f"Your order is {self.qunt} Jalebi")
            print(f"Amount: {self.price}")
        elif self.ch == 3:
            self.price = self.qunt * 130
            print(f"Your order is {self.qunt} Kheer")
            print(f"Amount: {self.price}")
        else:
            print("Please choose an available choice")


def file():
    with open("history.txt", "a") as out:
        out.write("order submit successfully.\n")
        print("Order Is Recorded")


def read():
    with open("history.txt", "r") as fp:
        print("Your Order History")
        for line in fp:
            print(line.strip())


def main():
    op = Option()
    while True:
        print("ORDER FOOD ONLINE AT HOME")
        print("1. MAKE ORDER")
        print("2. HISTORY")
        print("3. QUIT")
        ch = int(input("Choose Any One Option From List: "))

        if ch == 1:
            op.menu_list()
        elif ch == 2:
            read()
            return
        elif ch == 3:
            print("\nPress Enter To Exit")
            return
        else:
            print("Choice invalid...")

        print("\nPress 1 For Confirm Order")
        print("Press 0 For Cancel Order")
        user_entry = int(input("Press Here: "))
        if user_entry == 1:
            file()
        else:
            print("Order is canceled")

        print("\nPress 1 For Go Back Menu")
        user_entry = int(input("Press Here: "))
        if user_entry != 1:
            print("\nThanks for visiting us")
            break

_name_ = "_main_"
if _name_ == "_main_":
    main()


