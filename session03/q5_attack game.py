class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1
        
    def show_info(self):
        print(f"{self.name} | Level: {self.level} | power: {self.power} | health: {self.health} | coins: {self.coins}")

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        other.health = other.health - self.power
        print(f"{self.name} attack {other.name}. {other.name} health: {other.health}")

    def earn_coins(self, amount):
        self.coins = self.coins + amount

    def buy_potion(self):
        if self.coins >= 20:
            self.coins = self.coins -20
            self.health = self.health + 30
            print(f"{self.name} buy a potion")
        else:
            print("Not enough coins")

    def level_up(self):
        self.level = self.level + 1
        self.power = self.power + 5
        print(f"{self.name} level: {self.level}. new power: {self.power}")
    
duck =Character ("Duck", 10, 90, 40)
lion =Character ("Lion", 15, 100, 50)

lion.attack(duck)
duck.attack(lion)

lion.buy_potion()
duck.level_up()

print("info : ")
duck.show_info()
lion.show_info()
