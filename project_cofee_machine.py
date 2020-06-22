# Write your code here
# Author giri110890
class CoffeeMachine:
    available_amount_of_water = 400
    available_amount_of_milk = 540
    available_amount_of_beans = 120
    number_of_coffee_cups = 9
    money = 550
    state = None

    def perform_action(self, user_input):
        if user_input == "remaining":
            self.update_state()
            self.state = None
        elif user_input == "take":
            self.take()
            self.state = None
        elif user_input == "fill":
            self.state = "water"
        elif user_input == "buy":
            self.state = "buy"
        elif self.state == "buy":
            self.buy(user_input)
        elif self.state == "water":
            self.fill(user_input, 0, 0, 0)
        elif self.state == "milk":
            self.fill(0, user_input, 0, 0)
        elif self.state == "beans":
            self.fill(0, 0, user_input, 0)
        elif self.state == "cups":
            self.fill(0, 0, 0, user_input)

    def fill(self, water_amount_to_add=0, milk_amount_to_add=0, beans_amount_to_add=0, cups_to_add=0):
        if self.state == "water":
            self.available_amount_of_water += water_amount_to_add
            self.state = "milk"
        elif self.state == "milk":
            self.available_amount_of_milk += milk_amount_to_add
            self.state = "beans"
        elif self.state == "beans":
            self.available_amount_of_beans += beans_amount_to_add
            self.state = "cups"
        else:
            self.number_of_coffee_cups += cups_to_add
            self.state = None

    def buy(self, user_choice):
        if user_choice == str(1):
            if self.available_amount_of_water < 250:
                print("Sorry not enough water!")
                self.state = None
            elif self.available_amount_of_beans < 16:
                print("Sorry not enough beans!")
                self.state = None
            elif self.number_of_coffee_cups < 1:
                print("Sorry not enough disposable cups!")
                self.state = None
            else:
                self.available_amount_of_water -= 250
                self.available_amount_of_beans -= 16
                self.money += 4
                self.number_of_coffee_cups -= 1
                print("I have enough resources, making you a coffee!")
                self.state = None
        elif user_choice == str(2):
            if self.available_amount_of_water < 350:
                print("Sorry not enough water!")
                self.state = None
            elif self.available_amount_of_beans < 20:
                print("Sorry not enough beans!")
                self.state = None
            elif self.available_amount_of_milk < 75:
                print("Sorry not enough milk!")
                self.state = None
            elif self.number_of_coffee_cups < 1:
                print("Sorry not enough disposable cups!")
                self.state = None
            else:
                self.available_amount_of_water -= 350
                self.available_amount_of_milk -= 75
                self.available_amount_of_beans -= 20
                self.money += 7
                self.number_of_coffee_cups -= 1
                print("I have enough resources, making you a coffee!")
                self.state = None
        elif user_choice == str(3):
            if self.available_amount_of_water < 200:
                print("Sorry not enough water!")
                self.state = None
            elif self.available_amount_of_beans < 12:
                print("Sorry not enough beans!")
                self.state = None
            elif self.available_amount_of_milk < 100:
                print("Sorry not enough milk!")
                self.state = None
            elif self.number_of_coffee_cups < 1:
                print("Sorry not enough disposable cups!")
                self.state = None
            else:
                self.available_amount_of_water -= 200
                self.available_amount_of_milk -= 100
                self.available_amount_of_beans -= 12
                self.money += 6
                self.number_of_coffee_cups -= 1
                print("I have enough resources, making you a coffee!")
                self.state = None
        elif user_choice == "back":
            return

    def take(self):
        print("I gave you $" + str(self.money))
        self.money -= self.money

    def update_state(self):
        print("The coffee machine has:")
        print(self.available_amount_of_water, " of water")
        print(self.available_amount_of_milk, " of milk")
        print(self.available_amount_of_beans, " of coffee beans")
        print(self.number_of_coffee_cups, " of disposable cups")
        print(self.money, " of money")


coffee = CoffeeMachine()
while True:
    if coffee.state == "buy":
        user_action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee.perform_action(user_action)
    elif coffee.state == "water":
        user_action = int(input("Write how many ml of water do you want to add:"))
        coffee.perform_action(user_action)
    elif coffee.state == "milk":
        user_action = int(input("Write how many ml of milk do you want to add:"))
        coffee.perform_action(user_action)
    elif coffee.state == "beans":
        user_action = int(input("Write how many grams of coffee beans do you want to add:"))
        coffee.perform_action(user_action)
    elif coffee.state == "cups":
        user_action = int(input("Write how many disposable cups of coffee do you want to add:"))
        coffee.perform_action(user_action)
    else:
        user_action = input("Write action (buy, fill, take, remaining, exit):")
        if user_action == "exit":
            break
        else:
            coffee.perform_action(user_action)
