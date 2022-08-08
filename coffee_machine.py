class CoffeeMachine:

    def __init__(self):
        self.supplies = {"water": 400, "milk": 540, "coffee_beans": 120, "disposable_cups": 9, "money": 550}
        self.ingredients_for_coffee = {"water": [250, 350, 200], "milk": [0, 75, 100], "coffee_beans": [16, 20, 12],
                                       "disposable_cups": [1, 1, 1], "money": [-4, -7, -6]}
        self.ingredients = ["water", "milk", "coffee_beans", "disposable_cups", "money"]

    def condition(self):
        print(f"""The coffee machine has:
        {self.supplies["water"]} ml of water
        {self.supplies["milk"]} ml of milk
        {self.supplies["coffee_beans"]} g of coffee beans
        {self.supplies["disposable_cups"]} disposable cups
        ${self.supplies["money"]} of money""")

    def buy(self, coffee):
        for i in self.ingredients:
            if self.supplies[i] < self.ingredients_for_coffee[i][coffee - 1]:
                print(f"Sorry, not enough {i}!")
                return
        print("I have enough resources, making you a coffee!")
        for j in self.ingredients:
            self.supplies[j] -= self.ingredients_for_coffee[j][coffee - 1]

    def fill(self):
        self.supplies["water"] += int(input("Write how many ml of water you want to add:\n"))
        self.supplies["milk"] += int(input("Write how many ml of milk you want to add:\n"))
        self.supplies["coffee_beans"] += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.supplies["disposable_cups"] += int(input("Write how many disposable cups you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.supplies.get('money')}")
        self.supplies["money"] -= self.supplies["money"]


def main():
    coffee_machine = CoffeeMachine()
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main "
                           "menu:\n")
            if choice == "back":
                continue
            else:
                choice = int(choice)
                coffee_machine.buy(choice)
        elif action == "fill":
            coffee_machine.fill()
        elif action == "take":
            coffee_machine.take()
        elif action == "remaining":
            coffee_machine.condition()
        elif action == "exit":
            exit()


if __name__ == '__main__':
    main()
